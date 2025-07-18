import argparse
import os
import shutil
import datetime
import logging
import json
from multiprocessing import Queue

from src.utils.logger import configure_root_logger
from src.script_generator.common import load_json
from src.remote_utils.ssh_config import ssh_config_xrt
from src.remote_utils.remote_shell_template import RemoteShellTask
from src.remote_utils.remote_copy_template import RemoteCopyTask

LOG_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}

def run_script_api(dir: str):
    logger = logging.getLogger(__name__)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    shutil.make_archive(os.path.join(dir, 'all'), 'zip', dir)
    remote_dir =  os.path.join(f'/home/xrt/NetAutoTest', os.path.relpath(dir))
    remote_zip_path = os.path.join(remote_dir, 'all.zip')
    local_zip_path = os.path.join(dir, 'all.zip')

    upload_task = RemoteCopyTask(
        'Upload All',
        ssh_config_xrt,
        remote_zip_path,
        local_zip_path,
        is_download=False
    )

    upload_task.start()
    upload_task.wait_until_command_finish()
    logger.info('Upload file finished')

    run_task = RemoteShellTask(
        'Run Script',
        ssh_config_xrt,
        [
            {
                'command': 'cd ~/NetAutoTest && source ~/.bashrc && conda activate test\n',
                'finish_sign': '',
                'name': 'Setup Environment'
            },
            {
                'command': f'python response_sg.py -p {remote_dir}\n',
                'finish_sign': '====Response Finish Sign====',
                'name': 'Run Script'
            }
        ],
        f'./remote_logs/{current_time}.log',
        Queue()
    )
    run_task.start()
    run_task.wait_until_command_finish()
    run_task.signal_stop()
    while True:
        if run_task.try_join() == True: break

    remote_response_path = os.path.join(remote_dir, 'response.json')
    local_response_path = os.path.join(dir, 'response.json')

    download_task = RemoteCopyTask(
        'Download Response',
        ssh_config_xrt,
        remote_response_path,
        local_response_path,
        is_download=True
    )
    download_task.start()
    download_task.wait_until_command_finish()
    response = load_json(local_response_path)

    return response


def copy_case_files(tc_path, temp_dir):
    # Copy all files in the test case directory
    for fname in os.listdir(tc_path):
        src = os.path.join(tc_path, fname)
        dst = os.path.join(temp_dir, fname)
        if os.path.isfile(src):
            shutil.copy2(src, dst)
    # Copy testbed.json from the parent directory if not present in the test case directory
    upper_dir = os.path.dirname(tc_path)
    testbed_src = os.path.join(upper_dir, "testbed.json")
    testbed_dst = os.path.join(temp_dir, "testbed.json")
    if not os.path.exists(os.path.join(tc_path, "testbed.json")) and os.path.exists(testbed_src):
        shutil.copy2(testbed_src, testbed_dst)
    elif os.path.exists(os.path.join(tc_path, "testbed.json")):
        shutil.copy2(os.path.join(tc_path, "testbed.json"), testbed_dst)
    # If main.py does not exist but main_pass.py exists, copy main_pass.py as main.py
    main_py = os.path.join(temp_dir, "main.py")
    main_pass_py = os.path.join(temp_dir, "main_pass.py")
    if not os.path.exists(main_py) and os.path.exists(main_pass_py):
        shutil.copy2(main_pass_py, main_py)


def main():
    parser = argparse.ArgumentParser(description="Run the specified test case script")
    parser.add_argument("-p", "--path", required=True, help="Test case directory path")
    args = parser.parse_args()
    tc_path = args.path.rstrip("/")
    tc_name = os.path.basename(tc_path)
    now = datetime.datetime.now().strftime("%H-%M-%S")
    temp_dir = os.path.join("temp_script", f"{tc_name}_{now}")
    os.makedirs(temp_dir, exist_ok=True)
    copy_case_files(tc_path, temp_dir)
    # Call run_script_api
    result = run_script_api(temp_dir)
    print(result)

if __name__ == "__main__":
    main()