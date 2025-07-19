import os
import subprocess
import json

# Target directory
base_dir = 'example_results/configure_generation_examples'
# Result save path
result_json_path = './tc_result.json'

results = {}

# Traverse all folders starting with tc
tc_dirs = [d for d in os.listdir(base_dir) if d.startswith('tc') and os.path.isdir(os.path.join(base_dir, d))]
# tc_dirs = [d for d in tc_dirs if d == 'tc_6_5_10']
print(tc_dirs)

for tc_dir in tc_dirs:
    tc_path = os.path.join(base_dir, tc_dir)
    print(f'Running: python run_script.py -p {tc_path}')
    # Run script
    try:
        subprocess.run(['python', 'run_script.py', '-p', tc_path], check=True, timeout=600)
    except subprocess.TimeoutExpired:
        print(f'{tc_dir} run timeout (TLE)')
        results[tc_dir] = {'status': 'TLE', 'verdict': 'fail'}
        continue
    except subprocess.CalledProcessError as e:
        print(f'{tc_dir} run failed: {e}')
        results[tc_dir] = {'status': 'error', 'verdict': 'fail'}
        continue
    # Read response.json
    response_path = os.path.join(tc_path, 'response.json')
    if not os.path.exists(response_path):
        print(f'{tc_dir} did not generate response.json')
        results[tc_dir] = {'status': 'error', 'verdict': 'fail'}
        continue
    try:
        with open(response_path, 'r', encoding='utf-8') as f:
            resp = json.load(f)
        status = resp.get('status', '')
        verdict = resp.get('output', {}).get('verdict', '')
        # Normalize status
        if status != 'success': status = 'error'
        # Normalize verdict
        if verdict != 'pass': verdict = 'fail'
        results[tc_dir] = {'status': status, 'verdict': verdict}
    except Exception as e:
        print(f'{tc_dir} failed to parse response.json: {e}')
        results[tc_dir] = {'status': 'error', 'verdict': 'fail'}

# Save results
with open(result_json_path, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f'All results have been saved to {result_json_path}') 