import time
import paramiko
import re
from multiprocessing import Process, Queue, Value

from .ssh_config_template import *

def send_files(ssh_config: ssh_config_template, local_file_path, remote_file_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(ssh_config.private_key)
    try:
        ssh.connect(ssh_config.ip, ssh_config.port, ssh_config.username)
        sftp = ssh.open_sftp()
        sftp.put(local_file_path, remote_file_path)
    except Exception as e:
        print(f'Error in send_files: {e}')
    finally:
        ssh.close()

def run_shell_command(hostname, port, username, pkey, command_list, logdir, event_queue: Queue, stop_subprocess, polling_interval = 0.1):
    f = open(logdir, "w+")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port, username, pkey)
    shell = client.invoke_shell()
    shell.setblocking(0)

    for command in command_list:
        finish_sign_str = command["finish_sign"]
        shell_command = command["command"]
        command_name = command["name"]

        # print('\n', shell_command, '\n', file=f, flush=True)
        print(shell_command)
        shell.send(shell_command)
        while True:
            time.sleep(polling_interval)
            try:
                log_str = shell.recv(32768)
                log_str = log_str.decode("utf-8")
                print(log_str, end="\n", file=f, flush=True)
                # print(log_str)
                if re.search(finish_sign_str, log_str) != None:
                    time.sleep(1)
                    break
            except Exception as e:
                pass
        # print(f"\n{command_name} finished", file=f, flush=True)
        event_queue.put(command_name)
    
    while True:
        time.sleep(polling_interval)
        if stop_subprocess.value == 1:
            break
        try:
            log_str = shell.recv(32768)
            log_str = log_str.decode("utf-8")
            print(log_str, end="\n", file=f, flush=True)
            # print(log_str)
        except Exception as e:
            pass

class RemoteShellTask(object):
    def __init__(self, processname, ssh_config: ssh_config_template, command_list, logdir, event_queue, polling_interval = 0.1):
       self.processname = processname
       self.command_list = command_list
       self.stop_process = Value("l", 0)
       self.event_queue: Queue = event_queue
       self.process = Process(target=run_shell_command, args=(ssh_config.ip, ssh_config.port, ssh_config.username, ssh_config.private_key, command_list, logdir, event_queue, self.stop_process, polling_interval))

    def start(self):
        print(self.processname, "start")
        self.process.start()
    
    def wait_until_command_finish(self):
        for command in self.command_list:
            event = self.event_queue.get(block=True)
            if event != command["name"]:
                print("Error: event queue mismatch")
                print("Expected:", command["name"])
                print("Received:", event)
                print("Process:", self.processname)
            print(self.processname, event, "finished")

    def signal_stop(self):
        self.stop_process.value = 1
    
    def try_join(self):
        if not self.process.is_alive():
            print(self.processname, "join")
            self.process.join()
            return True
        return False
    
    def terminate(self):
        self.process.terminate()