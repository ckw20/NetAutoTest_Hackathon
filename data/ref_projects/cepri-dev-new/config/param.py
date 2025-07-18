import configparser
import os

dirname, tempfilename = os.path.split(os.path.abspath(__file__))
filename, extension = os.path.splitext(tempfilename)
CONFIG_FILE = os.path.abspath(os.path.join(dirname, 'param.cfg'))


class ParamCfg:
    pass


class Config:
    param = ParamCfg()

    @classmethod
    def parse(cls):
        conf = configparser.ConfigParser()
        if not os.path.exists(CONFIG_FILE):
            cls.save()
        conf.read(CONFIG_FILE)
        cls.param.match = conf.get('path', 'Match')
        cls.param.topu = conf.get('path', 'Topu')
        cls.param.device = conf.get('path', 'Device')
        cls.param.excel = conf.get('path', 'Excel')
        cls.param.temp = conf.get('path', 'Temp')
        cls.param.yaml = conf.get('path', 'Yaml')
        cls.param.variable = conf.get('path', 'Variable')
        cls.param.report = conf.get('path', 'Report')
        del conf

    @classmethod
    def save(cls):
        conf = configparser.ConfigParser()
        cfgfile = open(CONFIG_FILE, 'w')
        conf.add_section("path")
        conf.set("path", "Match", os.path.abspath(os.path.join(dirname, os.path.pardir, 'excel', 'Match.xlsx')))
        conf.set("path", "Topu", os.path.abspath(os.path.join(dirname, os.path.pardir, 'excel', 'Topu.xlsx')))
        conf.set("path", "Device", os.path.abspath(os.path.join(dirname, os.path.pardir, 'excel', 'Device.csv')))
        conf.set("path", "Excel", os.path.abspath(os.path.join(dirname, os.path.pardir, 'excel')))
        conf.set("path", "Temp", os.path.abspath(os.path.join(dirname, os.path.pardir, 'temp')))
        conf.set("path", "Yaml", os.path.abspath(os.path.join(dirname, os.path.pardir, 'yaml')))
        conf.set("path", "variable", os.path.abspath(os.path.join(dirname, os.path.pardir, 'yaml', 'variable.yaml')))
        conf.set("path", "Report", os.path.abspath(os.path.join(dirname, os.path.pardir, 'temp', 'report')))
        conf.write(cfgfile)
        cfgfile.close()
        del conf

    @classmethod
    def check(cls):
        if not os.path.exists(cls.param.variable):
            cls.save()


if __name__ == '__main__':
    Config.save()
