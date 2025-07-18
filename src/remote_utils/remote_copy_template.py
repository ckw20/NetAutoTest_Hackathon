import time
import paramiko
import os
from multiprocessing import Process, Queue, Value
from paramiko import SFTPClient

def create_remote_directories(sftp: SFTPClient, remote_path):
    dirname = os.path.dirname(remote_path)
    if dirname == '' or dirname == '/': return
    try:
        sftp.chdir(dirname)
    except IOError:
        create_remote_directories(sftp, dirname)
        sftp.mkdir(dirname)

def run_copy_command(hostname, port, username, pkey, remote_path, local_path, is_download):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port, username, pkey)
    shell = client.invoke_shell()
    shell.setblocking(0)

    sftp_client = client.get_transport().open_sftp_client()

    if is_download:
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        sftp_client.get(remote_path, local_path)
    else:
        create_remote_directories(sftp_client, remote_path)
        if os.path.isdir(local_path):
            for root, dirs, files in os.walk(local_path):
                remote_root = remote_path + root[len(local_path):]
                for d in dirs:
                    try:
                        sftp_client.stat(remote_root + "/" + d)
                    except FileNotFoundError:
                        sftp_client.mkdir(remote_root + "/" + d)
                for f in files:
                    sftp_client.put(root + "/" + f, remote_root + "/" + f)
        else:
            sftp_client.put(local_path, remote_path)
    

class RemoteCopyTask(object):
    def __init__(self, processname, ssh_config, remote_path, local_path, is_download):
        self.processname = processname
        self.remote_path = remote_path
        self.local_path = local_path
        self.is_download = is_download
        self.process = Process(target=run_copy_command, args=(ssh_config.ip, ssh_config.port, ssh_config.username, ssh_config.private_key, remote_path, local_path, is_download))

    def start(self):
        print(self.processname, "start")
        self.process.start()
    
    def wait_until_command_finish(self):
        while True:
            if self.process.is_alive():
                time.sleep(1)
            else:
                self.process.join()
                print(self.processname, "finished")
                break