import json, os, logging, argparse, shutil
logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description="Script Generation.")
    parser.add_argument("--config", type=str, required=True, help="Set to load config from a specific config file (json). See README.md for more details.")
    parser.add_argument("-l", "--log_level", type=str, default="DEBUG", help="The log level: DEBUG, INFO, WARNING, ERROR, CRITICAL.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode.")
    return parser.parse_args()

def args2cfg(args, current_time: str):
    config = load_json(args.config)
    config["current_time"] = current_time
    return config

def load_json(path: str, encoding: str | None = None):
    try:
        with open(path, "r", encoding=encoding) as f:
            result = json.load(f)
    except Exception as e:
        logger.error(f"In load_json({path}, {encoding}): {e}")
        with open(path, "r") as f:
            result = json.load(f)
    return result

def create_file_and_write(path: str, content: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as file: file.write(content)
    return os.path.abspath(path)

def copy_between(src_path: str, dst_path: str, file_name: str, from_src_to_dst: bool):
    try:
        if from_src_to_dst == True:
            os.makedirs(dst_path, exist_ok=True)
            shutil.copy(os.path.join(src_path, file_name), dst_path)
        else:
            os.makedirs(src_path, exist_ok=True)
            shutil.copy(os.path.join(dst_path, file_name), src_path)
    except shutil.SameFileError:
        pass
    except Exception as e:
        logger.debug(f'Error in copy_between(): {e}')

def save_results(cfg, result_code, history_codes, responses):
    dir = cfg['Task']['dir']
    tc_no = load_json(os.path.join(dir, 'cfg.json'))['tc_no']
    result_dir = f"./data/result_scripts/{tc_no}/{cfg['current_time']}/"
    shutil.copytree(dir, result_dir)
    create_file_and_write(os.path.join(result_dir, 'run_config.json'), json.dumps(cfg, indent=4, ensure_ascii=False))
    if result_code is not None:
        create_file_and_write(os.path.join(result_dir, 'main.py'), result_code)
    for iter in range(len(history_codes)):
        create_file_and_write(os.path.join(result_dir, f'main_iter_{iter + 1}.py'), history_codes[iter])
        create_file_and_write(os.path.join(result_dir, f'response_{iter + 1}.json'), json.dumps(responses[iter], indent=4, ensure_ascii=False))