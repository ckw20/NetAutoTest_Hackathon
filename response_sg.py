import os, argparse, json, shutil, tempfile
from src.validation.script_executor import run_test_script

def load_json(path: str, encoding = None):
    try:
        with open(path, "r", encoding=encoding) as f:
            result = json.load(f)
    except Exception as e:
        with open(path, "r") as f:
            result = json.load(f)
    return result

def copy_between(src_path: str, dst_path: str, file_name: str, from_src_to_dst: bool):
    # print(src_path, dst_path, file_name, from_src_to_dst)
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
        print(f'Error in copy_between(): {e}')

def move_the_fucking_cfg_testbed_device_setup_and_teardown_between_dir(
    all_file_in_one_dir: str, xet_repo_root_dir: str,testbed: dict, cfg: dict, from_src_to_dst: bool):
    tc_no = cfg['tc_no']
    duts = cfg['dut'] # ["DeviceA","DeviceB","DeviceC"]
    dut_cfgs: list[str] = cfg['dut_cfg'] # ["DeviceA_Setup","DeviceA_Teardown","DeviceB_Setup","DeviceB_Teardown","DeviceC_Setup","DeviceC_Teardown"]
    for dut in duts:
        if dut not in testbed['dut'].keys(): continue
        dut_type = testbed['dut'][dut]['dut_type'] # huawei_ce6881, etc
        command_path = os.path.join(xet_repo_root_dir, 'command', dut_type, tc_no)
        for dut_cfg in dut_cfgs:
            if dut_cfg.startswith(dut):
                copy_between(all_file_in_one_dir, command_path, dut_cfg + '.txt', from_src_to_dst)
    tc_no_path = os.path.join(xet_repo_root_dir, cfg['type'], tc_no)
    copy_between(all_file_in_one_dir, tc_no_path, 'main.py', from_src_to_dst)
    copy_between(all_file_in_one_dir, tc_no_path, 'cfg.json', from_src_to_dst)
    copy_between(all_file_in_one_dir,  os.path.join(xet_repo_root_dir, cfg['type']), 'testbed.json', from_src_to_dst)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Script Generation Response.")
    parser.add_argument('-p', '--path', type=str, help='all.zip containing all files(main.py, cfg.json, testbed.json, Device*_*.txt) shoule be under this path')
    args = parser.parse_args()
    dir = args.path
    zip_path = os.path.join(dir, 'all.zip')
    response_path = os.path.join(dir, 'response.json')

    with tempfile.TemporaryDirectory() as temp_dir:
        zip_copy_path = os.path.join(temp_dir, 'all_copy.zip')
        shutil.copy(zip_path, zip_copy_path)
        shutil.unpack_archive(zip_path, temp_dir, 'zip')
        if os.path.exists(dir): shutil.rmtree(dir)
        shutil.copytree(temp_dir, dir)
        os.remove(zip_path)
        os.rename(zip_copy_path, zip_path)
        os.remove(os.path.join(dir, 'all_copy.zip'))

    xet_repo_root_dir = '/home/xrt/NetAutoTest/data/ref_projects/cepri-dev-new'
    testbed = load_json(os.path.join(dir, 'testbed.json'))
    cfg = load_json(os.path.join(dir, 'cfg.json'))
    move_the_fucking_cfg_testbed_device_setup_and_teardown_between_dir(
        all_file_in_one_dir=dir,
        xet_repo_root_dir=xet_repo_root_dir,
        testbed=testbed,
        cfg=cfg,
        from_src_to_dst=True
    )

    main_path = os.path.join(xet_repo_root_dir, cfg['type'], cfg['tc_no'], 'main.py')
    response_ = run_test_script(
        main_path=main_path,
    )

    response = {
        "status": "success" if response_["return_value"] == 0 else "error",
        "message": response_["exception_error"],
        "output": {
            "file": response_["file"],
            "verdict": response_["verdict"],
            "errInfo": response_["errInfo"],
            "info": response_["info"]
        }
    }

    # response = {
    #     'qwq': 'gg'
    # }

    with open(response_path, 'w') as rf:
        rf.write(json.dumps(response, indent=4, ensure_ascii=False))

    print('====Response Finish Sign====') # MUST BE PRINTED!!!