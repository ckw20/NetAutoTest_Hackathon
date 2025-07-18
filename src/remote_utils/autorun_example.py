import os
from remote_utils.ssh_config import *


from remote_utils.remote_shell_template import *
from remote_utils.remote_copy_template import *

COMPILE_P4 = True

if __name__ == '__main__':
    if not os.path.exists("remote_logs"):
        os.mkdir("remote_logs")
        
    compile_tasks = []
    if COMPILE_P4 == True:
        compile_tasks.append(RemoteShellTask(
            "p4_compile",
            ssh_config_p4,
            [
                {
                    "command": "cd /root/temp/netbeacon/switch/p2p && sh p2p_compile.sh\n",
                    "finish_sign": "DONE",
                    "name": "compile"
                }
            ],
            "remote_logs/p4_compile.log",
            Queue()
        ))

        for task in compile_tasks: task.start()
        for task in compile_tasks: task.wait_until_command_finish()
        for task in compile_tasks: task.signal_stop()
        for task in compile_tasks:
            while True:
                ret = task.try_join()
                if ret == True: break
        print('compile finished.')


    # for t in [2, 4, 6, 8, 10]:
    for t in [2]:
        dataplane_steup = RemoteShellTask(
            "dataplane_setup",
            ssh_config_p4,
            [
                {
                    "command": "cd /root/temp/netbeacon/switch/p2p && sh p2p_dataplane.sh\n",
                    "finish_sign": "bfshell>",
                    "name": "p4_dataplane"
                }
            ],
            "remote_logs/p4_dataplane.log",
            Queue()
        )
        
        controlplane_setup = RemoteShellTask(
            "controlplane_setup",
            ssh_config_p4,
            [
                {
                    "command": "cd /root/temp/netbeacon/switch/p2p && sh p2p_controlplane.sh\n",
                    "finish_sign": "receive_digest",
                    "name": "p4_controlplane"
                }
            ],
            "remote_logs/p4_controlplane.log",
            Queue()
        )

        capture_pcap = RemoteShellTask(
            "capture_" + str(t) + "times",
            ssh_config_dc4new,
            [
                {
                    "command": "cd /home/ckw20/capture_pcap && sudo tshark -i enp1s0f1 -w ./result/netbeacon_p2p_using_depth_le8/netbeacon_p2p_" + str(t) + "times.pcap\ndc4qwqgg\n",
                    "finish_sign": "Capturing",
                    "name": "capture_" + str(t) + "times"
                }
            ],
            "remote_logs/capture_" + str(t) + "times.log",
            Queue()
        )
        
        replay_pcap = RemoteShellTask(
            "replay_" + str(t) + "times",
            ssh_config_dc6,
            [
                {
                    "command": "cd /home/dc6/pcaps && sudo tcpreplay -i enp1s0f1 --loop 1 p2p/p2p_1200s_" + str(t) + "times_ts.pcap\nhdu3302\n",
                    "finish_sign": "Statistics",
                    "name": "replay_" + str(t) + "times"
                }
            ],
            "remote_logs/replay_" + str(t) + "times.log",
            Queue()
        )
        dataplane_steup.start()
        dataplane_steup.wait_until_command_finish()
        print("dataplane setup")
        
        
        controlplane_setup.start()
        controlplane_setup.wait_until_command_finish()
        print("controlplane setup")
        
        capture_pcap.start()
        capture_pcap.wait_until_command_finish()
        
        replay_pcap.start()
        replay_pcap.wait_until_command_finish()
        print(str(t) + "times start replaying & capturing...")
        
        try_join_tasks = [replay_pcap, capture_pcap, dataplane_steup, controlplane_setup]
        for task in try_join_tasks:
            task.signal_stop()
            while True:
                if task.try_join() == True: break
        
        print(str(t) + 'times finished.\n')