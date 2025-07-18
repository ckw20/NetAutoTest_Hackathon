from openai import OpenAI
from src.utils.llm_agent import AgentBase
from src.testcase_generator.utils import parse_rsp, unify_id
from src.doc_parser.rfc_splitter import RFCNode
from src.validation.json_validator import validate_json, load_json
import logging
import json

logger = logging.getLogger(__name__)
LLM_MAX_TRIES = 3

class Testcase2JSON(AgentBase):
    """ 
    A test case to JSON converter agent to support non-structured test case examples.
    """ 
    def __init__(self, model='deepseek-v3'):
        super().__init__(model=model)
        self.name = "Testcase2JSON"
        logger.info("Testcase2JSON initialized.")
        self.prompt = """
### Task
Generate a test case in JSON format based on the following test case.

### Test Case
{testcase}

### Test Topology
{topo}

### Test Case JSON Template
{testcase_template}

### Test Case JSON Generation
```json (Your test case here)```
"""

    def testcase2json(self, testcase_path, testcase_template_path="data/testcases/examples/testcase_template_with_topology.json", topo_path="data/testcases/examples/one-tester-one-dut/topo_one.json"):
        self.clear_context()
        testcase_template = open(testcase_template_path, "r").read()
        topo = open(topo_path, "r").read()
        testcase = open(testcase_path, "r").read()
        prompt = self.prompt.format(testcase=testcase, testcase_template=testcase_template, topo=topo)
        logger.info(f"Prompt:\n{prompt}")
        res = None
        max_tries = LLM_MAX_TRIES
        while not res:
            max_tries -= 1
            if max_tries < 0:
                logger.error("Max tries exceeded.")
                break
            res = parse_rsp(self.response(prompt))
            logger.info(f"Response:\n{res}")
            res_json = json.loads(res)
            if validate_json(res_json, load_json(testcase_template_path.replace(".json", "_schema.json"))):
                break
            else:
                res = None
        return res

class TestPointGenerator(AgentBase):
    """ 
    A naive test case generator agent.
    1. Open-ended test point generation
    2. Test point generation under topology constraints
    """
    def __init__(self, model='deepseek-r1', testcase_point_example_path="data/testcases/examples/few_shot_of_testcase_points.json", testcase_point_template_path="data/testcases/examples/testcase_point_template.json", *args, **kwargs):
        super().__init__(model=model, *args, **kwargs)
        self.name = "TestPointGenerator"
        logger.info("TestPointGenerator initialized.")
        self.testcase_point_examples = open(testcase_point_example_path, "r").read()
        self.testcase_point_template = open(testcase_point_template_path, "r").read()
        self.testcase_point_schema = load_json(testcase_point_template_path.replace(".json", "_schema.json"))
        # 1. Open-ended test point generation
        self.prompt_analyze_test_point = """
### Task
Based on the following section of the RFC document to be tested, generate test points according to the template, including fields such as test case titles and test purposes. See the template for details.
Ensure the correctness and coverage of the test points. Ensure that the extracted relevant reference section numbers are legal.
The test case ID starts from 1 and increments.

### Example
{few_shot_point_examples}

### Content of the RFC Document Section to be Tested
{rfc_page_content}

### Content of the Relevant Reference Sections
{refs_content}

### Test Point Template
{testcase_point_template}

### Test Point Generation
```json (Your test case here)```
"""
        # 2. Test point generation under topology constraints
        self.prompt_analyze_test_point_with_topo = """
### Task
Based on the following section of the RFC document to be tested, generate test points according to the template, including fields such as test case titles and test purposes. See the template for details.
Ensure the correctness and coverage of the test points. Ensure that the extracted relevant reference section numbers are legal.
Ensure that the test points can be implemented on the given topology. If no test can be implemented in this section with the given test points, generate an empty JSON object.
The test case ID starts from 1 and increments.

### Example
{few_shot_point_examples}

### Target Topology
{topo}

### Content of the RFC Document Section to be Tested
{rfc_page_content}

### Content of the Relevant Reference Sections
{refs_content}

### Test Point Template
{testcase_point_template}

### Test Point Generation
```json (Your test case here)```
"""

    def analyze_test_point(self, rfc_root: RFCNode, target_id, section_refs, topo=None):
        """ First get the relevant reference sections, then generate test points. """

        self.clear_context()
        rfc_node = rfc_root.get_subnode_by_id(target_id)
        refs = json.loads(section_refs)
        refs_content = ""
        for id in refs:
            node = rfc_root.get_subnode_by_id(id)
            if node:
                refs_content += node.get_full_page() + "\n\n"
        if not topo:
            prompt_analyze_test_point = self.prompt_analyze_test_point.format(rfc_page_content=rfc_node.get_full_page(), refs_content=refs_content, few_shot_point_examples=self.testcase_point_examples, testcase_point_template=self.testcase_point_template)
        else:
            prompt_analyze_test_point = self.prompt_analyze_test_point_with_topo.format(rfc_page_content=rfc_node.get_full_page(), refs_content=refs_content, few_shot_point_examples=self.testcase_point_examples, testcase_point_template=self.testcase_point_template, topo=topo)
        logger.info(f"Prompt (generate test points):\n{prompt_analyze_test_point}")
        res = None
        max_tries = LLM_MAX_TRIES
        while not res:
            max_tries -= 1
            if max_tries < 0:
                logger.error("Max tries exceeded.")
                break
            res = parse_rsp(self.response(prompt_analyze_test_point))
            logger.info(f"Response (test points):\n{res}")
            res_json = json.loads(res)
            if not validate_json(res_json, self.testcase_point_schema):
                res = None
        return res


class NaiveTestCaseGenerator(AgentBase):
    """ 
    A naive test case generator agent. 
    """ 
    def __init__(self,  model='deepseek-v3'):
        super().__init__(model=model)
        self.name = "NaiveTestCaseGenerator"
        logger.info("NaiveTestCaseGenerator initialized.")
        self.max_try = 10

        # Zero-shot prompt
        self.prompt_naive = """
### Task
Based on the following section of the RFC document, generate test case steps according to the template.

### Content of the RFC Document Section to be Tested
{rfc_page_content}

### Test Case Template
{testcase_template}

### Test Case Generation
```json (Your test case here)```
"""
        # Few-shot prompt
        self.prompt_few_shot = """
### Task
Based on the following section of the RFC document, generate test case steps according to the template.

### Example
{few_shot_examples}

### Content of the RFC Document Section to be Tested
{rfc_page_content}

### Test Case Template
{testcase_template}

### Test Case Generation
```json (Your test case here)```
"""
        # Get references prompt
        self.prompt_get_refs = """
### Task
Extract the numbers of other sections that the following section of the RFC document depends on. Ensure that these numbers are correct, legal, and appear in the RFC document.
Please return a list containing the section numbers in the following format, without other information. 
For example: ```json ["1.1", "2.2"]```

### Content of the RFC Document Section to be Tested
{rfc_page_content}

### Extracted Section Numbers
```json (Your answer here)```
"""
        # Few-shot prompt with references
        self.prompt_few_shot_with_refs = """
### Task
Based on the following section of the RFC document to be tested, generate test case steps according to the template.
To generate more accurate test cases, we also provide the content of the relevant reference sections.
The test case ID starts from 1 and increments.

### Example
{few_shot_examples}

### Content of the RFC Document Section to be Tested
{rfc_page_content}

### Content of the Relevant Reference Sections
{refs_content}

### Test Case Template
{testcase_template}

### Test Case Generation
```json (Your test case here)```
"""
        # Testpoint guided prompt with references
        self.prompt_few_shot_with_testpoint_and_refs = """
### Task
Based on the following section of the RFC document to be tested, generate test case steps according to the template.
To generate more accurate test cases, we also provide the content of the relevant reference sections.
The test case ID starts from 1 and increments.

### Example
{few_shot_examples}

### Content of the RFC Document Section to be Tested
{rfc_page_content}

### Test Point
{testpoint}

### Content of the Relevant Reference Sections
{refs_content}

### Test Case Template
{testcase_template}

### Test Case Generation
```json (Your test case here)```
"""
        # Testpoint guided prompt with references and topo
        self.prompt_few_shot_with_testpoint_topo_and_refs = """
### Task
Based on the following section of the RFC document to be tested, generate test case steps according to the template.
The test cases need to be implemented on the given target topology, but do not include specific device names, etc. The generated test cases should be generic.
To generate more accurate test cases, we also provide the content of the relevant reference sections.

### Example
{few_shot_examples}

### Target Topology
{topo}

### Test Point
{testpoint}

### Content of the RFC Document Section to be Tested
{rfc_page_content}

### Content of the Relevant Reference Sections
{refs_content}

### Test Case Template
{testcase_template}

### Test Case Generation
```json (Your test case here)```
"""
        # Script configuration file generation prompt
        self.prompt_few_shot_of_cfg_file = """
## Task Description
Based on the following network device test case, generate the corresponding configuration JSON file (cfg.json) to define the interface parameters involved in the test case steps.
Generate the file by referring to the example content.

## Task Example
### Test Case
{few_shot_example}

### Corresponding JSON Configuration File
{cfg_example}

## Specific Task
#### Target Topology
{topo}

### Test Case
{testcase}

### Configuration JSON File Template
{cfg_template}

### Configuration JSON File Generation Result
```json (Your configuration here)```
"""
        # DUT configuration file generation prompt
        self.prompt_few_shot_of_dut_cfg = """
## Task Description
Based on the following network device test case, generate the corresponding configuration file for the Device Under Test (DUT) {device_type} for the {action}.
Generate the file by referring to the example content.

## Task Example
### Test Case
{few_shot_example}

### Corresponding JSON Configuration File
{cfg_example}

### DUT Configuration File
{cfg_dut_example}

## Specific Task
#### Target Topology
{topo}

### Test Case
{testcase}

### Corresponding JSON Configuration File
{cfg_file}

### DUT Configuration File Generation Result
```plaintext (Your DUT configuration here)```
"""
    def naive(self, rfc_node, testcase_template_path):
        self.clear_context()
        testcase_template = open(testcase_template_path, "r").read()
        prompt = self.prompt_naive.format(rfc_page_content=rfc_node.get_full_page(), testcase_template=testcase_template)
        logger.info(f"Prompt:\n{prompt}")
        return self.response(prompt)
    
    def few_shot(self, rfc_node, few_shot_example_path, testcase_template_path):
        self.clear_context()
        few_shot_example = open(few_shot_example_path, "r").read()
        testcase_template = open(testcase_template_path, "r").read()
        prompt = self.prompt_few_shot.format(rfc_page_content=rfc_node.get_full_page(), few_shot_examples=few_shot_example, testcase_template=testcase_template)
        logger.info(f"Prompt:\n{prompt}")
        return self.response(prompt)

    def get_refs(self, rfc_root: RFCNode, target_id) -> str:
        """ Get references of a given RFC section. """
        self.clear_context()
        rfc_node = rfc_root.get_subnode_by_id(target_id)
        prompt = self.prompt_get_refs.format(rfc_page_content=rfc_node.get_full_page())
        logger.info(f"Prompt:\n{prompt}")
        return parse_rsp(self.response(prompt))

    def few_shot_with_refs(self, rfc_root: RFCNode, target_id, few_shot_example_path, testcase_template_path):
        self.clear_context()
        rfc_node = rfc_root.get_subnode_by_id(target_id)
        refs = parse_rsp(self.get_refs(rfc_root, target_id))
        logger.info(f"Refs:\n{refs}")
        refs = json.loads(refs)
        refs_content = ""
        for id in refs:
            node = rfc_root.get_subnode_by_id(id)
            if node:
                refs_content += node.get_full_page() + "\n\n"
        self.clear_context()
        few_shot_examples = open(few_shot_example_path, "r").read()
        testcase_template = open(testcase_template_path, "r").read()
        prompt_few_shot_with_refs = self.prompt_few_shot_with_refs.format(rfc_page_content=rfc_node.get_full_page(), refs_content=refs_content, few_shot_examples=few_shot_examples, testcase_template=testcase_template)
        logger.info(f"Prompt (generate testcases):\n{prompt_few_shot_with_refs}")
        res = self.response(prompt_few_shot_with_refs)
        logger.info(f"Response (testcases):\n{res}")
        return res

    def few_shot_with_testpoint_and_refs(self, rfc_root: RFCNode, target_id, testpoint_json, few_shot_example_path, testcase_template_path, topo=None):
        self.clear_context()
        target_id = unify_id(target_id)
        rfc_node = rfc_root.get_subnode_by_id(target_id)
        testpoint = json.dumps(testpoint_json, ensure_ascii=False, indent=2)
        refs = testpoint_json['test_reference']
        refs_content = ""
        for id in refs:
            id = unify_id(id)
            if id == target_id:
                continue
            node = rfc_root.get_subnode_by_id(id)
            if node:
                refs_content += node.get_full_page() + "\n\n"
        self.clear_context()
        few_shot_examples = open(few_shot_example_path, "r").read()
        testcase_template = open(testcase_template_path, "r").read()
        if topo:
            prompt_few_shot_with_testpoints_and_refs = self.prompt_few_shot_with_testpoint_topo_and_refs.format(rfc_page_content=rfc_node.get_full_page(), refs_content=refs_content, few_shot_examples=few_shot_examples, testcase_template=testcase_template, testpoint=testpoint, topo=topo)
        else:
            prompt_few_shot_with_testpoints_and_refs = self.prompt_few_shot_with_testpoint_and_refs.format(rfc_page_content=rfc_node.get_full_page(), refs_content=refs_content, few_shot_examples=few_shot_examples, testcase_template=testcase_template, testpoint=testpoint)
        logger.info(f"Prompt (generate testcases):\n{prompt_few_shot_with_testpoints_and_refs}")
        res = None
        testcase_schema = load_json(testcase_template_path.replace(".json", "_schema.json"))
        max_tries = LLM_MAX_TRIES
        while not res:
            max_tries -= 1
            if max_tries < 0:
                logger.error("Max try exceeded.")
                break
            res = parse_rsp(self.response(prompt_few_shot_with_testpoints_and_refs))
            logger.info(f"Response (testcases):\n{res}")
            res_json = json.loads(res)
            if not validate_json(res_json, testcase_schema):
                res = None
        return res

    def few_shot_of_cfg_file(self, few_shot_example_path, cfg_example_path, cfg_template_path, topo, testcase):
        self.clear_context()
        few_shot_example = open(few_shot_example_path, "r").read()
        cfg_example = open(cfg_example_path, "r").read()
        cfg_template = open(cfg_template_path, "r").read()
        prompt_few_shot_of_cfg_file = self.prompt_few_shot_of_cfg_file.format(few_shot_example=few_shot_example, cfg_example=cfg_example, topo=topo, testcase=testcase, cfg_template=cfg_template)
        logger.info(f"Prompt (generate testcases):\n{prompt_few_shot_of_cfg_file}")
        res = None
        cfg_schema = load_json(cfg_template_path.replace(".json", "_schema.json"))
        max_tires = LLM_MAX_TRIES
        while not res:
            max_tires -= 1
            if max_tires < 0:
                logger.error("Max try exceeded.")
                break
            res = parse_rsp(self.response(prompt_few_shot_of_cfg_file))
            logger.info(f"Response (testcases):\n{res}")
            res_json = json.loads(res)
            if not validate_json(res_json, cfg_schema):
                res = None
        return res

    def few_shot_of_dut_cfg(self, few_shot_example_path, cfg_example_path, cfg_dut_example_path, cfg_path, topo_path, testcase, device_type, action):
        self.clear_context()
        few_shot_example = open(few_shot_example_path, "r").read()
        cfg_example = open(cfg_example_path, "r").read()
        cfg_dut_example = open(cfg_dut_example_path, "r").read()
        topo = open(topo_path, "r").read()
        cfg = open(cfg_path, "r").read()
        prompt_few_shot_of_dut_cfg = self.prompt_few_shot_of_dut_cfg.format(few_shot_example=few_shot_example, cfg_example=cfg_example, cfg_dut_example=cfg_dut_example, topo=topo, testcase=testcase, cfg_file=cfg, device_type=device_type, action=action)
        logger.info(f"Prompt (generate testcases):\n{prompt_few_shot_of_dut_cfg}")
        res = None
        max_tries = LLM_MAX_TRIES
        while not res:
            max_tries -= 1
            if max_tries < 0:
                logger.error("Max try exceeded.")
                break
            res = parse_rsp(self.response(prompt_few_shot_of_dut_cfg), fmt="plaintext")
            logger.info(f"Response (testcases):\n{res}")
        return res


class TestCaseJudger(AgentBase):
    """ 
    A test case judger agent. 
    """ 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "TestcaseJudger"
        logger.info("TestcaseJudger initialized.")
        self.prompt_testpoint_coverage = """
### Task Description
For the following relevant sections of the RFC, we have generated several test points. Please determine whether these test points fully cover all the important content specified in the RFC document, and supplement the missing test points.
The supplemented test points should maintain the same format as the original test points.
If the test points already fully cover all the important content specified in the RFC document, please directly return ```json {"test_case_points": []}```.

### Content of the RFC Document Section to be Tested
{rfc_page_content}

### Content of the Relevant Sections of the RFC Document to be Tested
{rfc_refs_content}

### Existing Test Points
{existing_testpoints}

### Supplemented Test Points
```json (Your added test point here)```
"""

        self.prompt_testpoint_coverage_with_topo = """
### Task Description
For the following relevant sections of the RFC, we have generated several test points. Please determine whether these test points fully cover all the important content specified in the RFC document, and supplement the missing test points.
The supplemented test points should maintain the same format as the original test points and follow the target topology constraints.
If the test points already fully cover all the important content specified in the RFC document, please directly return ```json {"test_case_points": []}```.

### Target Topology
{topo}

### Content of the RFC Document Section to be Tested
{rfc_page_content}

### Content of the Relevant Sections of the RFC Document to be Tested
{rfc_refs_content}

### Existing Test Points
{existing_testpoints}

### Supplemented Test Points
```json (Your added test point here)```
"""


        self.prompt_testcase_validation = """
### Task Description
Based on the following section of the RFC document, we have generated a test case. Please determine whether this test case is legal.
If it is legal, note the test basis (RFC original text) in the comments field; if it is not legal, note the reason for non-compliance in the comments field.

### Content of the RFC Document Section to be Tested
{rfc_page_content}

### Content of the Relevant Sections of the RFC Document to be Tested
{rfc_refs_content}

### Test Case
{testcase}

### Test Case Validation Result
```json {"valid": true/false, "comments": "Your comments here"}```
"""

        self.prompt_testcase_validation_with_topo = """
### Task Description
Based on the following section of the RFC document, we have generated a test case. Please determine whether this test case is legal.
If it is legal, note the test basis (RFC original text) in the comments field; if it is not legal, note the reason for non-compliance in the comments field.

### Target Topology
{topo}

### Content of the RFC Document Section to be Tested
{rfc_page_content}

### Content of the Relevant Sections of the RFC Document to be Tested
{rfc_refs_content}

### Test Case
{testcase}

### Test Case Validation Result
```json {"valid": true/false, "comments": "Your comments here"}```
"""
    
    def analyze_testpoint_coverage(self, rfc_root: RFCNode, target_id, section_refs, existing_testpoints, testcase_point_template_path, topo=None):
        self.clear_context()
        rfc_node = rfc_root.get_subnode_by_id(target_id)
        refs = json.loads(section_refs)
        refs_content = ""
        for id in refs:
            node = rfc_root.get_subnode_by_id(id)
            if node:
                refs_content += node.get_full_page() + "\n\n"
        # TODO: with topo
        if not topo:
            prompt_testpoint_coverage = self.prompt_testpoint_coverage.format(rfc_page_content=rfc_node.get_full_page(), rfc_refs_content=refs_content, existing_testpoints=existing_testpoints)
        else:
            prompt_testpoint_coverage = self.prompt_testpoint_coverage_with_topo.format(rfc_page_content=rfc_node.get_full_page(), rfc_refs_content=refs_content, existing_testpoints=existing_testpoints, topo=topo)
        logger.info(f"Prompt:\n{prompt_testpoint_coverage}")
        res = None
        max_tries = LLM_MAX_TRIES
        while not res:
            max_tries -= 1
            if max_tries < 0:
                logger.error("Max tries exceeded.")
                break
            res = parse_rsp(self.response(prompt_testpoint_coverage))
            logger.info(f"Response:\n{res}")
            if validate_json(json.loads(res), load_json(testcase_point_template_path.replace(".json", "_schema.json"))):
                break
            else:
                res = None
        return res

    def validate_testcase(self, rfc_root: RFCNode, target_id, section_refs, testcase, topo=None):
        self.clear_context()
        rfc_node = rfc_root.get_subnode_by_id(target_id)
        refs = json.loads(section_refs)
        refs_content = ""
        for id in refs:
            node = rfc_root.get_subnode_by_id(id)
            if node:
                refs_content += node.get_full_page() + "\n\n"
        if not topo:
            prompt_testcase_validation = self.prompt_testcase_validation.format(rfc_page_content=rfc_node.get_full_page(), rfc_refs_content=refs_content, testcase=testcase)
        else:
            prompt_testcase_validation = self.prompt_testcase_validation_with_topo.format(rfc_page_content=rfc_node.get_full_page(), rfc_refs_content=refs_content, testcase=testcase, topo=topo)
        logger.info(f"Prompt:\n{prompt_testcase_validation}")
        res = None
        max_tries = LLM_MAX_TRIES
        while not res:
            max_tries -= 1
            if max_tries < 0:
                logger.error("Max tries exceeded.")
                break
            res = parse_rsp(self.response(prompt_testcase_validation))
            logger.info(f"Response:\n{res}")
            if validate_json(json.loads(res), json.loads("""{"type":"object","properties":{"valid":{"type":"boolean"},"comments":{"type":"string"}},"required":["valid","comments"]}""")):
                break
            else:
                res = None
        return res


class FSMExtractor(AgentBase):
    """ 
    A finite state machine extractor agent. 
    """ 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "FSMExtractor"
        logger.info("FSMExtractor initialized.")
        self.prompt_fsm_extraction = """
## Task Description
Please extract the finite state machine (FSM) from the following OSPF RFC text, and output it strictly in JSON format:
1. List all states (states)
2. List all events (events)
3. Describe the state transition rules (transitions), including:
    - from_state (current state)
    - to_state (target state)
    - event (trigger event)
    - actions (executed actions)
4. Mark key constraints (such as timers, network types)
5. Use '*' to represent any state (for example: forced transition from any state to Down)

## Task Requirements
- Merge state machines according to requirements
- Include forced transition events (such as KillNbr)
- Use the original RFC text to describe actions

## RFC Text
{rfc_text}

## Output Format Template
{fsm_template}

## Extraction Result
```json (Your FSM here)```
"""

        self.prompt_fsm_supplement = """
## Task Description
Please supplement the finite state machine (FSM) from the following OSPF RFC text, and output it strictly in JSON format:
1. List all states (states)
2. List all events (events)
3. Describe the state transition rules (transitions), including:
    - from_state (current state)
    - to_state (target state)
    - event (trigger event)
    - actions (executed actions)
4. Mark key constraints (such as timers, network types)
5. Use '*' to represent any state (for example: forced transition from any state to Down)

## Task Requirements
- Supplement the missing parts in the existing state machine
- Include forced transition events (such as KillNbr)
- Use the original RFC text to describe actions
- Output the JSON description of the entire supplemented state machine
- If the existing state machine is already complete, return an empty JSON object

## RFC Text
{rfc_text}

## Existing State Machine
{fsm_json}

## Supplemented Extraction Result
```json (Your FSM here)```
"""

    def extract_fsm(self, rfc_text, fsm_template_path="data/parsed_documents/RFC_FSMs/fsm_template.json"):
        self.clear_context()
        fsm_template = open(fsm_template_path, "r").read()
        prompt = self.prompt_fsm_extraction.format(rfc_text=rfc_text, fsm_template=fsm_template)
        logger.info(f"Prompt:\n{prompt}")
        
        res = None
        max_tries = LLM_MAX_TRIES
        json_schema = load_json(fsm_template_path.replace(".json", "_schema.json"))
        while not res:
            max_tries -= 1
            if max_tries < 0:
                logger.error("Max tries exceeded.")
                break
            res = parse_rsp(self.response(prompt))
            logger.info(f"Response:\n{res}")
            if validate_json(json.loads(res), json_schema):
                break
            else:
                res = None
        return res
    
    def supplement_fsm(self, rfc_text, fsm_json, fsm_template_path="data/parsed_documents/RFC_FSMs/fsm_template.json"):
        self.clear_context()
        prompt = self.prompt_fsm_supplement.format(rfc_text=rfc_text, fsm_json=fsm_json)
        logger.info(f"Prompt:\n{prompt}")
        
        res = None
        max_tries = LLM_MAX_TRIES
        json_schema = load_json(fsm_template_path.replace(".json", "_schema.json"))
        while not res:
            max_tries -= 1
            if max_tries < 0:
                logger.error("Max tries exceeded.")
                break
            res = parse_rsp(self.response(prompt))
            logger.info(f"Response:\n{res}")
            if validate_json(json.loads(res), json_schema):
                break
            else:
                res = None
        return res

class TestCaseGenFromFSM(AgentBase):
    """ 
    A finite state machine to test case agent. 
    """ 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "FSM2TestCase"
        logger.info("FSM2TestCase initialized.")
        self.prompt_fsm_testcase_gen = """
### Task
Based on the following path of the finite state machine (FSM) to be tested extracted from the RFC, generate test case steps according to the template.
To generate more accurate test cases, we also provide the content of the relevant RFC section.
Since the FSM path is continuous, to ensure the test case is executable, it is necessary to explain how to put the device into the state to be tested.
Therefore, the entire given FSM path needs to be tested in **one** complete test case.
The expected results of the steps should be measurable.

### Example
{few_shot_examples}

### Content of the RFC Document Section to be Tested
{rfc_page_content}

### FSM Path to be Tested
{fsm_path}

### Test Case Template
{testcase_template}

### Test Case Generation
```json (Your test case here)```
"""

        self.prompt_fsm_testcase_gen_with_topo = """
### Task
Based on the following path of the finite state machine (FSM) to be tested extracted from the RFC, generate test case steps according to the template.
To generate more accurate test cases, we also provide the content of the relevant RFC section.
Since the FSM path is continuous, to ensure the test case is executable, it is necessary to explain how to put the device into the state to be tested.
Therefore, the entire given FSM path needs to be tested in **one** complete test case.
The expected results of the steps should be measurable.

### Test Case Example
{few_shot_examples}

### Content of the RFC Document Section to be Tested
{rfc_page_content}

### Target Topology
{topo}

### FSM Path to be Tested
{fsm_path}

### Test Case Template
{testcase_template}

### Test Case Generation
```json (Your test case here)```
"""
    def fsm2testcase(self, few_shot_example_path, rfc_page_content_path, fsm_path, testcase_template_path, topo_path=None):
        self.clear_context()
        few_shot_example = open(few_shot_example_path, "r").read()
        rfc_page_content = open(rfc_page_content_path, "r").read()
        testcase_template = open(testcase_template_path, "r").read()
        if topo_path:
            topo = open(topo_path, "r").read()
            prompt_fsm_testcase_gen = self.prompt_fsm_testcase_gen_with_topo.format(rfc_page_content=rfc_page_content, fsm_path=fsm_path, few_shot_examples=few_shot_example, testcase_template=testcase_template, topo=topo)
        else:
            prompt_fsm_testcase_gen = self.prompt_fsm_testcase_gen.format(rfc_page_content=rfc_page_content, fsm_path=fsm_path, few_shot_examples=few_shot_example, testcase_template=testcase_template)
        logger.info(f"Prompt:\n{prompt_fsm_testcase_gen}")
        res = None
        max_tries = LLM_MAX_TRIES
        more_than_one = False
        while not res:
            max_tries -= 1
            if max_tries < 0:
                logger.error("Max tries exceeded.")
                break
            if more_than_one:
                res = parse_rsp(self.response("Please generate ONLY ONE test case."))   # Multi-round dialogue
            else:
                res = parse_rsp(self.response(prompt_fsm_testcase_gen))
            res_json = json.loads(res)
            logger.info(f"Response:\n{res}")
            if validate_json(res_json, load_json(testcase_template_path.replace(".json", "_schema.json"))):
                if len(res_json['test_cases']) == 1:
                    break
                else:
                    more_than_one = True
                    logger.warning("More than one test case generated, retring...")
                    res = None
            else:
                res = None
                logger.warning("Invalid test case generated, retring...")
                self.clear_context()
        return res
    

class TestCaseGenFromField(AgentBase):
    """ 
    A test case generator agent from fields. 
    """ 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "TestCaseGenFromfield"
        logger.info("TestCaseGenFromfield initialized.")
        # Extract header fields
        self.prompt_extract_fields = """
### Task
Based on the following section of the RFC document, extract the protocol packet field information, including the packet name, field names, and relevant description information.
The field constraint information includes but is not limited to the field value range, constraint conditions for specific values, etc. Do not list this information separately, but put it in a natural language description string.
The involved constraint information should be as detailed and verifiable as possible.
Please return a list containing the field names and description information according to the given template, without other information.

### Content of the RFC Document Section to be Extracted
{field_page_content}

### Protocol Packet Field Template
{packet_field_template}

### Extracted Protocol Packet Fields
```json (Your answer here)```
"""
        # Extract relevant reference sections of the header
        self.prompt_get_refs = """
### Task
Extract the numbers of other sections that the following section of the RFC document depends on. Ensure that these numbers are correct, legal, and appear in the RFC document.
Please return a list containing the section numbers in the following format, without other information.
For example: ```json ["1.1", "2.2"]```

### Content of the RFC Document Section to be Tested
{field_page_content}

### Extracted Section Numbers
```json (Your answer here)```
"""
        # Extract field constraints
        self.prompt_extract_constraints = """
### Task
Based on the following section of the RFC document, extract the constraint conditions of the protocol packet fields.
Supplement the extracted constraint conditions in the given header field JSON file.
The field constraint information includes but is not limited to all possible values of the field, the length of the field, the type of the field, etc. But do not list this information separately, but put it in a natural language description string.
The involved constraint information should be as detailed as possible, but do not repeat the content of other fields (such as description, number of bits, etc.).
If the newly extracted constraint information can be merged with the original constraint information, merge it into the original constraint information.
Please ensure that the extracted constraint information is correct, legal, and appears in the RFC document. Do not fabricate or infer.
Keep all other content of the original JSON.

### Content of the RFC Document Section to be Extracted
{field_page_content}

### Protocol Packet Field JSON File
{field_json}

### Protocol Packet Field JSON File after Supplementing Constraint Conditions
```json (Your answer here)```
"""

        # Generate test cases (and topology) based on packet fields and constraints
        self.prompt_testcase_gen_from_field_with_topo = """
### Task
Based on the following relevant information such as the **protocol packet fields to be tested and their constraints** extracted from the RFC, generate test case steps according to the template.
To generate more accurate test cases, we also provide the content of the relevant RFC section.
The expected results of the steps should be measurable.

### Test Case Content Requirements
- The test cases need to cover all constraints of the packet fields to be tested, including positive and negative tests.
- The test cases should not include any tests related to fields other than the specified packet fields.
- The first step of the test case should be "Initialize the device test environment according to the provided configuration". The relevant specific configuration is placed in the appendix field.
- The test cases need to include test steps and expected results. Only add test results in the **key steps**, and do not add expected results for each step.
- The expected results of each step should be **measurable in the tester** and should not directly access the device under test.
- The steps of a single test case should not be too many, and the implementation difficulty should be consistent with the existing test cases.
- Use the smallest possible topology to implement the test.
- If there are multiple test points (such as positive and negative tests), they need to be split into **multiple test cases**.

### Test Case Format Requirements
- The generated test cases should be as consistent in style with the existing test cases as possible and avoid repetition.
- Different test cases should be independent and should not reference each other's content.
- The generated test cases should include the minimum topology that supports the implementation of the test case.
- The test case ID starts from 1 and increments.

### Existing Test Case Examples
{few_shot_examples}

### Relevant Content of the RFC Document to be Tested
{rfc_page_content}

### Protocol Packet Fields to be Tested and Their Constraints
{packet_field}

### Test Case Template
{testcase_template}

### Test Case Generation Result
```json (Your test case here)```
"""

    def extract_packet_fields(self, field_page_path, packet_field_template_path):
        self.clear_context()
        field_content = open(field_page_path, "r").read()
        field_template = open(packet_field_template_path, "r").read()
        prompt = self.prompt_extract_fields.format(field_page_content=field_content, packet_field_template=field_template)
        logger.info(f"Prompt:\n{prompt}")
        res = None
        max_tries = LLM_MAX_TRIES
        while not res:
            max_tries -= 1
            if max_tries < 0:
                logger.error("Max tries exceeded.")
                break
            res = parse_rsp(self.response(prompt))
            logger.info(f"Response:\n{res}")
            schema = load_json(packet_field_template_path.replace(".json", "_schema.json"))
            if validate_json(json.loads(res), schema):
                break
            else:
                res = None
                logger.warning("Invalid packet fields generated, retring...")
                self.clear_context()
        return res
    
    def get_refs(self, field_page_path) -> str:
        """ Get references of a given RFC section. """
        self.clear_context()
        field_page_content = open(field_page_path, "r").read()
        prompt = self.prompt_get_refs.format(field_page_content=field_page_content)
        logger.info(f"Prompt:\n{prompt}")
        res = None
        max_tries = LLM_MAX_TRIES
        while not res:
            max_tries -= 1
            if max_tries < 0:
                logger.error("Max tries exceeded.")
                break
            try:
                res = parse_rsp(self.response(prompt))
                json.loads(res)
            except json.JSONDecodeError:
                res = None
                logger.warning("Invalid JSON format, retring...")
                self.clear_context()
            logger.info(f"Refs:\n{res}")
        return res
    
    def extract_constraints(self, field_json_path, field_page_content, field_template_path):
        self.clear_context()
        field_json_str = open(field_json_path, "r").read()
        prompt = self.prompt_extract_constraints.format(field_page_content=field_page_content, field_json=field_json_str)
        logger.info(f"Prompt:\n{prompt}")
        res = None
        max_tries = LLM_MAX_TRIES
        while not res:
            max_tries -= 1
            if max_tries < 0:
                logger.error("Max tries exceeded.")
                break
            res = parse_rsp(self.response(prompt))
            logger.info(f"Response:\n{res}")
            try:
                schema = load_json(field_template_path.replace(".json", "_schema.json"))
                if validate_json(json.loads(res), schema):
                    break
            except Exception as e:
                logger.error(f"Error: {e}")
                logger.warning("Invalid JSON format, retring...")
                res = None
                self.clear_context()
        return res

    def field2testcase(self, few_shot_example_path, rfc_page_content_path, packet_field_constraint, testcase_template_path, topo_path=None):
        self.clear_context()
        few_shot_example = open(few_shot_example_path, "r").read()
        rfc_page_content = open(rfc_page_content_path, "r").read()
        testcase_template = open(testcase_template_path, "r").read()
        if topo_path:
            topo = open(topo_path, "r").read()
            # prompt_testcase_gen_from_field = self.prompt_testcase_gen_from_field_with_topo.format(rfc_page_content=rfc_page_content, packet_field=packet_field_constraint, few_shot_examples=few_shot_example, testcase_template=testcase_template, topo=topo)
            raise NotImplementedError("Test case generation from field with topology is not implemented yet.")
            pass
        else:
            prompt_testcase_gen_from_field = self.prompt_testcase_gen_from_field_with_topo.format(rfc_page_content=rfc_page_content, packet_field=packet_field_constraint, few_shot_examples=few_shot_example, testcase_template=testcase_template)
        logger.info(f"Prompt:\n{prompt_testcase_gen_from_field}")
        res = None
        max_tries = LLM_MAX_TRIES
        while not res:
            max_tries -= 1
            if max_tries < 0:
                logger.error("Max tries exceeded.")
                break
            res = parse_rsp(self.response(prompt_testcase_gen_from_field))
            logger.info(f"Response:\n{res}")
            schema = load_json(testcase_template_path.replace(".json", "_schema.json"))
            if validate_json(json.loads(res), schema):
                break
            else:
                res = None
                logger.warning("Invalid test case generated, retring...")
                self.clear_context()
        return res

class TestCaseGenFromStd(AgentBase):
    """ 
    A test case generator agent from standards. 
    """ 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "TestCaseGenFromStd"
        logger.info("TestCaseGenFromStd initialized.")
        self.prompt_get_content_id = """
### Task
Based on the following test case, extract the relevant chapter numbers from the RFC table of contents for reference to expand the test case.
The returned chapter numbers must exist in the RFC table of contents and only contain numbers and decimal points.
For example: ["1.1", "2.2"]

### Test Case
{testcase}

### RFC Table of Contents
{rfc_index}

### Extracted Chapter Numbers
Return a list containing section numbers in the following format.
```json (Your answer here)```
"""

        self.prompt_testcase_gen_from_std_without_topo = """
### Task
Expand test cases on the specified topology based on the following RFC chapter content.

### Test Point Requirements
- Try to挖掘 (mine) important details in the RFC chapter to ensure the correctness and coverage of the test cases.

### Test Case Content Requirements
- The test case needs to include test steps and expected results. Only add test results in key steps; there is no need to add expected results for each step.
- The expected result of each step should be measurable in the tester and should not directly access the device under test.
- A single test case should not have too many steps, and the implementation difficulty should be consistent with existing test cases.
- The first step of the test case should be "Initialize the device test environment according to the provided configuration". Place relevant specific configurations in the appendix field.

### Test Case Format Requirements
- The generated test cases should try to maintain a consistent style with existing test cases and avoid duplication.
- Different test cases should be independent and should not reference content from each other.
- The topology included in the generated test case should be a subset of the given target topology.
- New test case IDs start incrementing from 1.

### RFC Chapter Content
{rfc_page_content}

### Existing Test Cases
{testcase}

### Target Topology
{topo}

### Test Case Template
{testcase_template}

### Test Case Generation
Return a JSON object that conforms to the test case template in the following format. If expansion is not possible, return an empty JSON object.
```json (Your test case here)```
"""

    def get_content_id(self, std_testcase_path, rfc_index):
        self.clear_context()
        testcase = open(std_testcase_path, "r").read()
        prompt = self.prompt_get_content_id.format(testcase=testcase, rfc_index=rfc_index)
        logger.info(f"Prompt:\n{prompt}")
        res = None
        max_tries = LLM_MAX_TRIES
        while not res:
            max_tries -= 1
            if max_tries < 0:
                logger.error("Max tries exceeded.")
                break
            res = parse_rsp(self.response(prompt))
            logger.info(f"Response:\n{res}")
            try:
                if validate_json(json.loads(res), json.loads("""{"type":"array","items":{"type":"string","minLength":1},"minItems":1}""")):
                    break
                else:
                    res = None
                    logger.warning("Invalid section IDs generated, retring...")
                    self.clear_context()
            except json.JSONDecodeError:
                res = None
                logger.warning("Invalid JSON format, retring...")
                self.clear_context()
        return res

    def std2testcase(self, rfc_root, related_section, std_testcase_path, testcase_template_path, topo_path):
        """Expand test cases"""
        self.clear_context()
        rfc_node = rfc_root.get_subnode_by_id(related_section)
        rfc_page_content = rfc_node.get_full_page()
        std_testcase = open(std_testcase_path, "r").read()
        testcase_template = open(testcase_template_path, "r").read()
        topo = open(topo_path, "r").read()
        prompt_std2testcase = self.prompt_testcase_gen_from_std_with_topo.format(rfc_page_content=rfc_page_content, testcase=std_testcase, topo=topo, testcase_template=testcase_template)
        logger.info(f"Prompt:\n{prompt_std2testcase}")
        res = None
        max_tries = LLM_MAX_TRIES
        while not res:
            max_tries -= 1
            if max_tries < 0:
                logger.error("Max tries exceeded.")
                break
            res = parse_rsp(self.response(prompt_std2testcase))
            logger.info(f"Response:\n{res}")
            try:
                res_json = json.loads(res)
                if not res_json:
                    return "{}"
                if validate_json(res_json, load_json(testcase_template_path.replace(".json", "_schema.json"))):
                    break
                else:
                    res = None
                    logger.warning("Invalid test case generated, retring...")
                    self.clear_context()
            except json.JSONDecodeError:
                res = None
                logger.warning("Invalid JSON format, retring...")
                self.clear_context()
        return res
        

class TestCaseTranslator(AgentBase):
    """ 
    A test case translator agent. 
    """ 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "TestCaseTranslator"
        logger.info("TestCaseTranslator initialized.")
        self.prompt_testcase_translation = """
### Task Description
Please translate the following test case into {langurage}.

### Test Case
{testcase}

### Translation Result
```json (Your translated test case here)```
"""

    def translate_testcase(self, testcase_path, language='English', testcase_template_path='data/testcases/examples/testcase_template_with_topology.json'):
        self.clear_context()
        testcase = open(testcase_path, "r").read()
        prompt_testcase_translation = self.prompt_testcase_translation.format(testcase=testcase, langurage=language)
        logger.info(f"Prompt:\n{prompt_testcase_translation}")
        res = None
        max_tries = LLM_MAX_TRIES
        testcase_schema = load_json(testcase_template_path.replace(".json", "_schema.json"))
        while not res:
            max_tries -= 1
            if max_tries < 0:
                logger.error("Max tries exceeded.")
                break
            res = parse_rsp(self.response(prompt_testcase_translation))
            logger.info(f"Response (translated test case):\n{res}")
            try:
                # json.loads(res)
                if validate_json(json.loads(res), testcase_schema):
                    break
                else:
                    res = None
                    logger.warning("Invalid test case generated, retring...")
                    self.clear_context()
            except json.JSONDecodeError:
                res = None
                logger.warning("Invalid JSON format, retring...")
                self.clear_context()
        return res

class TestcaseFormator(AgentBase):
    """ 
    A test case formator agent. 
    """ 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "TestcaseFormator"
        logger.info("TestcaseFormator initialized.")
        self.prompt_tc_formator = """
### Task Description
Please convert the test case described in natural language into JSON format based on the following test case JSON template, test topology and other information.

### Test Case Described in Natural Language
{testcase}

### Test Case JSON Template
{testcase_template}

### Target Topology
{topo}

### Examples of JSON Format Test Cases
{testcase_example}

### Test Case JSON Formatting Result
```json (Your test case here)```
"""

    def format_testcase(self, testcase_path, topo_path, testcase_template_path, testcase_example_path):
        """Format test cases"""
        self.clear_context()
        testcase = open(testcase_path, "r").read()
        topo = open(topo_path, "r").read()
        testcase_template = open(testcase_template_path, "r").read()
        testcase_example = open(testcase_example_path, "r").read()

        prompt_tc_formator = self.prompt_tc_formator.format(testcase=testcase, topo=topo, testcase_template=testcase_template, testcase_example=testcase_example)
        logger.info(f"Prompt:\n{prompt_tc_formator}")

        res = None
        max_tries = LLM_MAX_TRIES
        testcase_schema = load_json(testcase_template_path.replace(".json", "_schema.json"))
        while not res:
            max_tries -= 1
            if max_tries < 0:
                logger.error("Max tries exceeded.")
                break
            res = parse_rsp(self.response(prompt_tc_formator))
            logger.info(f"Response:\n{res}")
            try:
                if validate_json(json.loads(res), testcase_schema):
                    if len(json.loads(res)['test_cases']) == 1:
                        break
                    else:
                        logger.info("More than one test case generated, retring...")
                else:
                    res = None
                    logger.warning("Invalid test case generated, retring...")
                    self.clear_context()
            except json.JSONDecodeError:
                res = None
                logger.warning("Invalid JSON format, retring...")
                self.clear_context()
        return res