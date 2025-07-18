# NeTestLLM

Large Language Model Driven Automated Network Protocol Testing
 
## Main Module Introduction
- `src.doc_parser`: Document parsing
- `src.testcase_generator`: Test case generation
- `src.script_generator`: Script generation
- `src.validation`: Validation and feedback

## Requirements
```
openai=1.60.1
jsonschema==4.23.0
```
Alibaba Cloud DashScope LLM service platform API key: Set it in the environment variable `DASHSCOPE_API_KEY=your_api_key`

### Code Generation
**It is highly recommended to install PyTorch manually to avoid version inconsistencies of CUDA-related tools. For details, refer to the [PyTorch official website](https://pytorch.org/get-started/locally/).**


It is recommended to install the environment in conda to avoid environment conflicts:

```shell
conda create -n test python=3.11.9
conda activate test
pip3 install -r requirements_sg_py.txt
```

or：

```shell
conda create -n test python=3.11.9
conda activate test
conda install --file requirements_sg_conda.txt
```

## Usage
### 1. Test Case Generation

- Applicable to scenarios where test cases are generated from protocol specifications.
- To generate code from existing test cases, start from step 2.

#### 1.1 Data Preparation
1. Download standard document (e.g., RFC) texts, put them into the data/raw_documents folder.
2. Extract the parts to be tested from standard Q&A (e.g., protocol packet fields, finite state machines, etc.), put them into the data/parsed_documents folder.
3. Select relevant industry standards/enterprise standard test cases, put them into the data/testcases/examples folder. Refer to the corresponding JSON template for formatting.

#### 1.2 Protocol Understanding and Test Case Generation
Full Pipeline: Take the Hello packet of OSPF protocol as an example.
```bash
python main_cg.py \
    --method field \
    --rfc-file data/raw_documents/RFCs/rfc2328.txt \
    --field-file data/parsed_documents/RFC_fields/rfc2328/A.3.2/text.txt \
    --testbed-path data/testcases/examples/one-tester-one-dut/testbed_one.json \
    --std-file data/testcases/examples/one-tester-one-dut/tc_6_7_6/cepri_tc_6_7_6.txt
```
The generated protocol field parsing file is located in the same directory as `field-file`.
The generated test cases are located in the `result` folder.

##### 1.2.1 Protocol Understanding
Protocol Field Understanding:
```bash
python main_cg.py \
    --method field \
    --sub-step understanding \
    --rfc-file data/raw_documents/RFCs/rfc2328.txt \
    --use-content-table \
    --field-file data/parsed_documents/RFC_fields/rfc2328/A.3.2/text.txt 
```

##### 1.2.2 Test Case Generation from Protocol Understanding
Protocol Field Test Case Generation:
```bash
python main_cg.py \
    --method field \
    --sub-step testcase-gen \
    --rfc-file data/raw_documents/RFCs/rfc2328.txt \
    --field-file data/parsed_documents/RFC_fields/rfc2328/A.3.2/text.txt \
    --field-json data/parsed_documents/RFC_fields/rfc2328/A.3.2/text_header.json \
    --std-file data/testcases/examples/one-tester-one-dut/tc_6_7_6/cepri_tc_6_7_6.txt
```

#### 1.3 Generation of Tester and DUT-related Configuration Files
Replace `testcase-path` with the path of a test case generated in the result folder.
```bash
python main_cg.py \
    --method addcfgs \
    --rfc-file data/raw_documents/RFCs/rfc2328.txt \
    --testcase-path example_results/2025-07-18-11-49-56_qwen-max-latest_rfc2328_Packet_fields/A.3.2_Hello_Packet/HelloInterval/testcases.json \
    --testbed-path data/testcases/examples/one-tester-one-dut/testbed_one.json \
    --topo-path data/testcases/examples/one-tester-one-dut/topo_one.json
```
The generated configuration files are located in the same directory as the JSON file in testcase-path, with a separate folder for each test case. The correctness of the configuration files needs to be checked manually.


### 2 Configuration Generation from Existing Test Cases (Optional)

- Applicable to the scenario of inputting existing test cases. The generated files include: formatted test cases, DUT configuration files, tester automation script configuration files
- Just replace the path of the test case to be tested with --testcase-path
- By default, the test is performed under the topology of one tester with one DUT. If you need to change the topology/testbed information, please replace the --testbed-path and --topo-path files

```bash
python main_cg.py \
    --method from_existing \
    --testcase-path data/testcases/existing/tc_2_1_2_1_1.txt \
    --testbed-path data/testcases/examples/one-tester-one-dut/testbed_one.json \
    --topo-path data/testcases/examples/one-tester-one-dut/topo_one.json
```

### 3 Test Code Generation

The directory structure for each test case (e.g., `tc1`, `tc2`, ...) is as follows:

```text
example_results/configure_generation_examples/tc*/
├── main.py           # Main test script to be executed
├── cfg.json          # Test configuration file
├── testbed.json      # Testbed (topology/environment) description
├── Device*_*.txt     # Device [A-Z] command configuration file(s), including Setup, Teardown and Step*
└── ...               # Additional device or auxiliary files
```

- `main.py`: The entry point script for running the test case.
- `cfg.json`: Contains parameters and settings for the test.
- `testbed.json`: Describes the test environment, including devices and connections.
- `Device*_*.txt`: Command configuration files for each device involved in the test.

Once you have prepared the necessary files in the `example_results/configure_generation_examples/tc*` directories (including `main.py`, `cfg.json`, `testbed.json`, and `Device*_*.txt`), you can use the `run_script.py` script to execute the test code automatically.

**Usage:**

```bash
python run_script.py -p <path_to_test_script_directory>
```
E.g.,

```bash
python run_script.py -p ./example_results/configure_generation_examples/tc_ospf_area_id_positive
```

- `<path_to_test_script_directory>` should be the path to the directory containing the generated test case files (e.g., `example_results/configure_generation_examples/tc1`).
- The directory must include at least `main.py`, `cfg.json`, `testbed.json`, and one or more `Device*_*.txt`.

The script will execute the test script remotely and download the result file (`response.json`) back to the local directory.

---

**Result Location and response.json Structure**

After execution, the result file `response.json` will be saved in the same directory as the test script (e.g., `example_results/configure_generation_examples/tc*/response.json`).

The structure of `response.json` is as follows:

```json
{
    "status": "success",           // Overall execution status: "success" or "fail"
    "message": "",                  // Error or information message (if any)
    "output": {
        "file": "...",             // Path to the executed main.py file
        "verdict": "fail",         // Test verdict: "pass", "fail"
        "errInfo": "...",          // Error information or exception details
        "info": "..."              // Detailed execution log and output
    }
}
```

- `status`: Indicates whether the test ran successfully.
- `message`: Provides additional information or error messages.
- `output.file`: The path to the executed test script.
- `output.verdict`: The final test result (e.g., pass/fail).
- `output.errInfo`: Any error or failure details encountered during execution.
- `output.info`: Detailed logs and information from the test process.
