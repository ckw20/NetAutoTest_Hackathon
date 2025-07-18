import subprocess, sys, os, re

def parse_log(log: str, user_filepath: str):
    """
    解析脚本日志，提取 verdict / errInfo / 异常信息 / 完整日志
    """
    verdict_match = re.search(r"verdict:\s*(.+)", log)
    verdict = verdict_match.group(1).strip() if verdict_match else ""
    err_info = ""
    exception_error = "success"

    if verdict:
        # 有 verdict 时提取 errInfo 区块
        err_info_match = re.search(r"errInfo:\s*\n(.*?)(?=\n\S+:|verdict:|\Z)", log, re.DOTALL)
        if err_info_match:
            err_info_raw = err_info_match.group(1)
            err_info_lines = [line.strip() for line in err_info_raw.splitlines() if line.strip()]
            err_info = "\n".join(err_info_lines)
    else:
        # 无 verdict，代表脚本运行失败，尝试匹配异常信息
        exception_error = "error"
        exception_match = re.search(r"^(Exception|KeyError):\s?.*$", log, re.MULTILINE)
        if exception_match:
            exception_error = exception_match.group(0).strip()

    return {
        "file": user_filepath,
        "verdict": verdict,
        "errInfo": err_info,
        "info": log,
        "exception_error": exception_error
    }

def run_test_script(main_path: str, timeout: int = 1200):
    """
    执行指定的 main.py 测试脚本，并返回统一的输出结构
    """
    def result_output(file_path, verdict, err_info, info, exception_error, return_code):
        return {
                "file": file_path,
                "verdict": verdict,
                "errInfo": err_info,
                "info": info,
                "exception_error": exception_error,
                "return_value": return_code
        }

    print("main_path", main_path)

    if main_path is None or not os.path.exists(main_path):
        return result_output(
            file_path=main_path,
            verdict="",
            err_info="Invalid path or file not found",
            info="",
            exception_error="路径无效或文件未找到",
            return_code=1
        )

    try:
        workdir = os.path.dirname(main_path)
        print(f"🚀 Executing script: {main_path}")
        # print(f"📂 Working directory: {workdir}")

        process = subprocess.Popen(
            ["python3", main_path],
            # capture_output=True,
            text=True,
            # timeout=timeout,
            cwd=workdir,
            encoding="utf-8",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        #
        # print("✅ Script execution completed")
        # print("📤 stdout:\n", result.stdout)
        # print("📤 stderr:\n", result.stderr)

        stdout_lines = []
        stderr_lines = []

        while True:
            stdout_line = process.stdout.readline() if process.stdout is not None else None
            stderr_line = process.stderr.readline() if process.stderr is not None else None
            if stdout_line:
                sys.stdout.write(stdout_line)
                stdout_lines.append(stdout_line)
            if stderr_line:
                sys.stderr.write(stderr_line)
                stderr_lines.append(stderr_line)
            if process.poll() is not None:
                break

        if process.stdout is not None:
            for line in process.stdout:
                sys.stdout.write(line)
                stdout_lines.append(line)
        if process.stderr is not None:
            for line in process.stderr:
                sys.stderr.write(line)
                stderr_lines.append(line)

        result_stdout = "".join(stdout_lines)
        result_stderr = "".join(stderr_lines)
        result_returncode =  process.returncode

        combined_log = result_stdout + "\n" + result_stderr
        log_result = parse_log(combined_log, main_path)

        return_code = result_returncode
        # 脚本失败（无 verdict 或 return_code 非 0）
        if return_code != 0 or log_result["exception_error"] != "success":
            return result_output(
                file_path=main_path,
                verdict="",
                err_info="",
                info=log_result["info"],
                exception_error=log_result["exception_error"],
                return_code=1
            )

        # ✅ 正常执行返回
        return result_output(
            file_path=main_path,
            verdict=log_result["verdict"],
            err_info=log_result["errInfo"],
            info=log_result["info"],
            exception_error="",
            return_code=0
        )

    except subprocess.TimeoutExpired:
        return result_output(
            file_path=main_path,
            verdict="",
            err_info="",
            info="",
            exception_error="Script execution timed out",
            return_code=1
        )

    except Exception as e:
        return result_output(
            file_path=main_path,
            verdict="",
            err_info="",
            info="",
            exception_error=f"Exception occurred: {str(e)}",
            return_code=1
        )


# # ✅ 示例调用
# result = run_test_script(
#     main_path=r"C:\Tsinghua\cepri-dev\cepri-dev\Testcase\tc_6_6_2\main.py"
# )

# print(json.dumps(result, indent=2, ensure_ascii=False))
