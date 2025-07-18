import os.path
import configparser
import os
import subprocess
import sys
import fire


class VersionCfg:
    pass


class Config:
    conf = configparser.ConfigParser()
    version = VersionCfg()

    @classmethod
    def parse_version(cls, Dir=False):
        if Dir:
            dirname, tempfilename = os.path.split(os.path.abspath(__file__))
            cls.conf.read(os.path.abspath(f'{dirname}/version.cfg'))
        else:
            cls.conf.read(os.path.abspath(f'{os.getcwd()}/version.cfg'))
        print(os.path.abspath('version.cfg'))
        cls.version.tag = cls.conf.get('version', 'tag')


class Version:
    base_index = 100000

    def __init__(self, Base=None, ProjectDir=None, Dir=False):
        if Base is not None:
            self.base_index = Base
        self.project_dir = ProjectDir
        self.dir = Dir

    @property
    def version(self):
        return '{}.{}'.format(self.get_tag(self.dir), self.get_version())

    @staticmethod
    def get_cmd_log(Cmd, WorkDir=None):
        buffer = ''
        cwd = os.getcwd()
        try:
            if WorkDir is not None:
                os.chdir(WorkDir)
            buffer = subprocess.check_output(Cmd, shell=True).decode(encoding='GBK', errors='ignore')
        except Exception as e:
            print(repr(e))
        finally:
            # print(buffer)
            os.chdir(cwd)
            return buffer

    def get_head_index(self, Head=None):
        if Head is None:
            Head = 'HEAD'
        return int(self.get_cmd_log(f'git rev-list --count {Head}', self.project_dir))

    def get_index_head(self, Index=None):
        max_count = self.get_head_index()
        if Index is None:
            Index = max_count
        head_list = self.get_cmd_log(f'git rev-list --max-count={max_count} HEAD', self.project_dir).split('\n')
        head = head_list[max_count - Index]
        return self.get_cmd_log(f'git rev-parse --short {head}', self.project_dir).replace('\n', '')

    def get_version(self, Head=None):
        return self.base_index + self.get_head_index(Head)

    def get_head(self, Version=None):
        if Version is not None:
            Version = Version - self.base_index
        return self.get_index_head(Version)

    @staticmethod
    def get_tag(Dir=False):
        Config.parse_version(Dir)
        return Config.version.tag

    def save(self):
        with open(os.path.join(os.getcwd(), 'version.txt'), mode='w+', encoding='utf-8') as fid:
            list_version = self.get_tag().split('.')
            list_version.append(str(self.get_version()))
            print('head: {}'.format(self.get_head()))
            print('versionCode: {}'.format(self.get_version()))
            for i in list_version:
                fid.write(f'{i}\n')
            print(os.path.join(os.getcwd(), 'version.txt'))


def test():
    version = Version()
    index = version.get_head_index()
    print(index)
    head = version.get_index_head()
    print(head)

    index = version.get_head_index('4ef4ea4')
    print(index)
    head = version.get_index_head(index)
    print(head)

    index = version.get_head_index('7b5e693fb0ace3be1d5d1bb86a85e8a903e064c8')
    print(index)
    head = version.get_index_head(index)
    print(head)

    result = version.get_version()
    print(result)
    result = version.get_head()
    print(result)

    result = version.get_version('4ef4ea4')
    print(result)
    result = version.get_head(result)
    print(result)

    result = version.get_version('7b5e693fb0ace3be1d5d1bb86a85e8a903e064c8')
    print(result)
    result = version.get_head(result)
    print(result)

    result = version.get_tag()
    print(result)


if __name__ == '__main__':
    fire.Fire(Version)
