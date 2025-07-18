import logging, datetime, os, json, shutil
os.environ["TOKENIZERS_PARALLELISM"] = "false"
from src.utils.logger import configure_root_logger
from src.script_generator.common import load_json, parse_args, args2cfg, save_results
from src.script_generator import generate_script
from src.remote_utils.ssh_config import *
from src.remote_utils.remote_shell_template import *
from src.remote_utils.remote_copy_template import *

LOG_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}
current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
TESTENV_SSH_CONFIG = ssh_config_xrt

# The dir should contains main.py, cfg.json, testbed.json, Device*_*.txt
def run_script_api(dir: str):
    logger = logging.getLogger(__name__)
    shutil.make_archive(os.path.join(dir, 'all'), 'zip', dir)
    remote_dir =  os.path.join(f'/home/xrt/NetAutoTest', os.path.relpath(dir))
    remote_zip_path = os.path.join(remote_dir, 'all.zip')
    local_zip_path = os.path.join(dir, 'all.zip')

    upload_task = RemoteCopyTask(
        'Upload All',
        TESTENV_SSH_CONFIG,
        remote_zip_path,
        local_zip_path,
        is_download=False
    )

    upload_task.start()
    upload_task.wait_until_command_finish()
    logger.info('Upload file finished')

    run_task = RemoteShellTask(
        'Run Script',
        TESTENV_SSH_CONFIG,
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
        TESTENV_SSH_CONFIG,
        remote_response_path,
        local_response_path,
        is_download=True
    )
    download_task.start()
    download_task.wait_until_command_finish()
    response = load_json(local_response_path)

    return response

if __name__ == "__main__":
    args = parse_args()
    if not os.path.exists("logs"): os.mkdir("logs")
    if not os.path.exists("remote_logs"): os.mkdir("remote_logs")

    configure_root_logger(
        filename=f"logs/{current_time}.log",
        level=LOG_LEVELS[args.log_level],
        format_str="[%(asctime)s] %(name)-25s %(levelname)-8s %(message)s" if args.verbose else "%(message)s"
    )
    logger = logging.getLogger(__name__)

    cfg: dict = args2cfg(args, current_time)
    logger.debug(f"cfg = {json.dumps(cfg, indent=4)}\n")

    result_code, history_codes, responses = generate_script(cfg, run_script_api)
    logger.debug(f'================ result code =================\n{result_code}')

    save_results(cfg, result_code, history_codes, responses)