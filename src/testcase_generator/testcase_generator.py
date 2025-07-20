import logging
import os
from src.doc_parser.rfc_purifier import purify_rfc
from src.doc_parser.rfc_splitter import RFCNode, build_rfc_tree
from .llm_agents import NaiveTestCaseGenerator, TestPointGenerator, TestCaseJudger, TestCaseGenFromFSM, TestCaseGenFromField, TestCaseGenFromStd, TestCaseTranslator, TestcaseFormator
from src.validation.json_validator import validate_json, load_json
import json

logger = logging.getLogger(__name__)

LLM_REFINE_MAX = 10   # Maximum iteration rounds for LLM refinement

def generate_test_cases_from_rfc(rfc_file_path, section, testcases_output_path, current_time, model="qwen-max-latest", topo_path=None, testpoint_path=None, testbed_path=None):
    """
    Generate test cases for a given RFC document section.
    """

    # Test point generation
    testcase_point_example_path="data/testcases/examples/few_shot_of_testcase_points.json"
    testcase_point_template_path="data/testcases/examples/testcase_point_template.json"
    # Case without topology constraints
    few_shot_examples_path="data/testcases/examples/few_shot_of_testcases_with_topology.json"
    testcase_template_path="data/testcases/examples/testcase_template_with_topology.json"
    # Case with topology constraints
    few_shot_example_wo_topo_path="data/testcases/examples/one-tester-one-dut/few_shot_of_testcases_without_topology.json"
    testcase_template_wo_topo_path="data/testcases/examples/one-tester-one-dut/testcase_template_without_topology.json"
    # Configuration generation
    few_shot_example_cfg_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/few_shot_of_testcase_with_topo_one_6_7_6.json"
    cfg_example_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/cfg.json"
    cfg_template_path="data/testcases/examples/one-tester-one-dut/cfg_template.json"
    # DUT configuration generation
    cfg_dut_testcase_example_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/few_shot_of_testcase_with_topo_one_6_7_6.json"
    cfg_dut_setup_example_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/dut_config/DeviceA_Setup.txt"
    cfg_dut_teardown_example_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/dut_config/DeviceA_Teardown.txt"

    # RFC document preprocessing
    if not os.path.exists(rfc_file_path.replace('.txt', '_purified.txt')):
        purify_rfc(rfc_file_path, None)   # None defaults to generating _purified.txt file

    # Build RFC tree
    rfc_root = build_rfc_tree(rfc_file_path.replace('.txt', '_purified.txt'))

    # Check RFC tree parsing results
    logger.info('RFC tree:')
    logger.info(rfc_root.print_subtree())
    logger.debug(rfc_root.get_subnode_by_id(section).get_full_page())

    # Output folder under /results, create folder with current time, output filename as input_file+section    
    if not os.path.exists("results"):
        os.mkdir("results")
    output_dir = f"results/{current_time}_{model}_{rfc_file_path.split('/')[-1].replace('.txt', '')}_{section}"
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # 1. Extract references for RFC node
    naive_generator = NaiveTestCaseGenerator()
    section_refs = naive_generator.get_refs(rfc_root, section)
    logger.info(f"Section {section} references: {section_refs}")

    # Case with topology constraints
    if topo_path: 
        topo = open(topo_path, "r").read()
        if not testpoint_path:
            # 2.1 Analyze test points based on given topology
            testpoint_generator = TestPointGenerator(model='deepseek-r1', testcase_point_example_path=testcase_point_example_path, testcase_point_template_path=testcase_point_template_path)
            testpoints = testpoint_generator.analyze_test_point(rfc_root, section, section_refs, topo)
            logger.info(f"Test points: {testpoints}")

            # 2.2. Iteratively analyze test point coverage
            testpoints_json = json.loads(testpoints)
            testcase_judger = TestCaseJudger(model='deepseek-r1')
            tries_cnt = 0
            while True:
                testpoints_plus = testcase_judger.analyze_testpoint_coverage(rfc_root, section, section_refs, json.dumps(testpoints_json, indent=2, ensure_ascii=False), testcase_point_template_path, topo)
                testpoints_plus_json = json.loads(testpoints_plus)
                if not testpoints_plus_json['test_case_points']:
                    break
                testpoints_json['test_case_points'] += testpoints_plus_json['test_case_points']
                tries_cnt += 1
                if tries_cnt > LLM_REFINE_MAX:
                    logger.info(f"Exceed maximum iteration times: {LLM_REFINE_MAX}")
                    break
            testpoints = json.dumps(testpoints_json, indent=2, ensure_ascii=False)

        else:
            testpoints = open(testpoint_path, "r").read()

        testcase_points_output_path = f"{output_dir}/{rfc_file_path.split('/')[-1].replace('.txt', '')}_{section}_testpoints.json" if testcases_output_path is None else testcases_output_path.replace('.json', '_testpoints.json')

        with open(testcase_points_output_path, 'w', encoding='utf-8') as f_out:
            f_out.write(testpoints)

        logger.info(f"Test points generation finished: {testpoints}")
        # exit()

        testpoints_json = json.loads(testpoints)
        for testpoint in testpoints_json['test_case_points']:
            # 3. Generate test cases based on given topology (in separate folders, in order)
            max_tries = 3
            while True:
                # 3.1. Generate test case
                logger.info(f"Generating test cases for test point:")
                logger.info(testpoint)

                testcase = naive_generator.few_shot_with_testpoint_and_refs(rfc_root, section, testpoint, few_shot_example_wo_topo_path, testcase_template_wo_topo_path, topo)

                # 3.2. Validate test case
                logger.info(f"Validating test case...")
                testcase_judger = TestCaseJudger(model='deepseek-v3')
                res = testcase_judger.validate_testcase(rfc_root, section, section_refs, testcase, topo)
                res_json = json.loads(res)
                if not res_json['valid']:
                    logger.error(f"Test case is invalid: {res}")
                    max_tries -= 1
                    if max_tries == 0:
                        break   # Abandon this test point
                    continue
                logger.info(f"Test case is valid: {res}")

                testpoint_path = os.path.join(output_dir, testpoint['id'])
                if not os.path.exists(testpoint_path):
                    os.mkdir(testpoint_path)

                testcases_output_path = f"{testpoint_path}/{rfc_file_path.split('/')[-1].replace('.txt', '')}_{section}_{testpoint['id']}.json"
                with open(testcases_output_path, 'w', encoding='utf-8') as f_out:
                    f_out.write(testcase)

                # A. Attach Testbed file
                testbed = None
                if testbed_path:
                    testbed = open(testbed_path, "r").read()
                    testbed_path = f"{testpoint_path}/testbed.json"
                    with open(testbed_path, 'w', encoding='utf-8') as f_out:
                        f_out.write(testbed)

                # 4. Generate cfg.json configuration file based on examples
                cfg = naive_generator.few_shot_of_cfg_file(few_shot_example_cfg_path, cfg_example_path, cfg_template_path, topo, testcase)
                cfg_path = f"{testpoint_path}/cfg.json"
                with open(cfg_path, 'w', encoding='utf-8') as f_out:
                    f_out.write(cfg)

                # 5. Generate DUT configuration files (Setup and Teardown) based on examples
                if testbed:
                    testbed_json = json.loads(testbed)
                    cfg_json = json.loads(cfg)
                    for device_name in cfg_json['dut']:
                        device_type = testbed_json['dut'][device_name]['dut_type']
                        # Generate Setup configuration file
                        setup_cfg = naive_generator.few_shot_of_dut_cfg(cfg_dut_testcase_example_path, cfg_example_path, cfg_dut_setup_example_path, cfg_path, topo, testcase, device_type, 'Setup')
                        setup_cfg_path = f"{testpoint_path}/{device_name}_Setup.txt"
                        with open(setup_cfg_path, 'w', encoding='utf-8') as f_out:
                            f_out.write(setup_cfg)
                        # Generate Teardown configuration file
                        teardown_cfg = naive_generator.few_shot_of_dut_cfg(cfg_dut_testcase_example_path, cfg_example_path, cfg_dut_teardown_example_path, cfg_path, topo, testcase, device_type, 'Teardown')
                        teardown_cfg_path = f"{testpoint_path}/{device_name}_Teardown.txt"
                        with open(teardown_cfg_path, 'w', encoding='utf-8') as f_out:
                            f_out.write(teardown_cfg)
                break   # Test case generation successful
    # Case without topology constraints
    else:
        # 2.1 Analyze test points
        testpoint_generator = TestPointGenerator(model='deepseek-r1', testcase_point_example_path=testcase_point_example_path, testcase_point_template_path=testcase_point_template_path)
        testpoints = testpoint_generator.analyze_test_point(rfc_root, section, section_refs)
        logger.info(f"Test points (initial): {testpoints}")

        # 2.2 Iteratively analyze test point coverage
        # # Test
        # with open("results/2025-03-17-23-14-06_qwen-max-latest_rfc2328_9.5/rfc2328_9.5_testpoints.json", 'r', encoding='utf-8') as f_in:
        #     testpoints = f_in.read()

        testpoints_json = json.loads(testpoints)
        testcase_judger = TestCaseJudger(model='deepseek-r1')
        tries_cnt = 0
        while True:
            testpoints_plus = testcase_judger.analyze_testpoint_coverage(rfc_root, section, section_refs, json.dumps(testpoints_json, indent=2, ensure_ascii=False), testcase_point_template_path)
            testpoints_plus_json = json.loads(testpoints_plus)
            if not testpoints_plus_json['test_case_points']:
                break
            testpoints_json['test_case_points'] += testpoints_plus_json['test_case_points']
            tries_cnt += 1
            if tries_cnt > LLM_REFINE_MAX:
                break

        testpoints = json.dumps(testpoints_json, indent=2, ensure_ascii=False)

        testcase_points_output_path = f"{output_dir}/{rfc_file_path.split('/')[-1].replace('.txt', '')}_{section}_testpoints.json" if testcases_output_path is None else testcases_output_path.replace('.json', '_testpoints.json')

        with open(testcase_points_output_path, 'w', encoding='utf-8') as f_out:
            f_out.write(testpoints)

        # 3. Generate and validate test cases
        testpoints_json = json.loads(testpoints)
        for testpoint in testpoints_json['test_case_points']:
            max_tries = 3
            while True:
                # 3.1. Generate test case
                logger.info(f"Generating test cases for test point:")
                logger.info(testpoint)

                testcase = naive_generator.few_shot_with_testpoint_and_refs(rfc_root, section, testpoint, few_shot_examples_path, testcase_template_path)
                
                # 3.2. Validate test case
                logger.info(f"Validating test case...")
                testcase_judger = TestCaseJudger(model='deepseek-v3')
                res = testcase_judger.validate_testcase(rfc_root, section, section_refs, testcase)
                res_json = json.loads(res)
                if not res_json['valid']:
                    logger.error(f"Test case is invalid: {res}")
                    max_tries -= 1
                    if max_tries == 0:
                        break   # Abandon this test point
                    continue
                logger.info(f"Test case is valid: {res}")

                testpoint_path = os.path.join(output_dir, testpoint['id'])
                if not os.path.exists(testpoint_path):
                    os.mkdir(testpoint_path)

                testcases_output_path = f"{testpoint_path}/{rfc_file_path.split('/')[-1].replace('.txt', '')}_{section}_{testpoint['id']}.json"
                with open(testcases_output_path, 'w', encoding='utf-8') as f_out:
                    f_out.write(testcase)

                break   # Test case generation successful
    return output_dir


def generate_test_cases_from_fsm(fsm_path, rfc_pate_content_path, current_time, model='qwen-max-latest', topo_path=None, testbed_path=None):

    # Case without topology constraints
    few_shot_examples_path="data/testcases/examples/few_shot_of_testcases_with_topology.json"
    testcase_template_path="data/testcases/examples/testcase_template_with_topology.json"    
    # Case with topology constraints
    few_shot_example_wo_topo_path="data/testcases/examples/one-tester-one-dut/few_shot_of_testcases_without_topology.json"
    testcase_template_wo_topo_path="data/testcases/examples/one-tester-one-dut/testcase_template_without_topology.json"
    # Configuration generation
    few_shot_example_cfg_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/few_shot_of_testcase_with_topo_one_6_7_6.json"
    cfg_example_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/cfg.json"
    cfg_template_path="data/testcases/examples/one-tester-one-dut/cfg_template.json"
    # DUT configuration generation
    cfg_dut_testcase_example_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/few_shot_of_testcase_with_topo_one_6_7_6.json"
    cfg_dut_setup_example_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/dut_config/DeviceA_Setup.txt"
    cfg_dut_teardown_example_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/dut_config/DeviceA_Teardown.txt"

    fsm_json = load_json(fsm_path)

    # Output folder under /results, create folder with current time, output filename as input_file+section    
    if not os.path.exists("results"):
        os.mkdir("results")
    output_dir = f"results/{current_time}_{model}_{fsm_path.split('/')[-1].replace('.json', '')}"

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    if topo_path:   # Case with topology constraints
        for i, path in enumerate(fsm_json):
            generator = TestCaseGenFromFSM(model=model)
            path_str = json.dumps(path, indent=2, ensure_ascii=False)
            testcase = generator.fsm2testcase(few_shot_example_wo_topo_path, rfc_pate_content_path, path_str, testcase_template_wo_topo_path, topo_path)

            testcase_dir = os.path.join(output_dir, f"testcase_{i+1}")
            if not os.path.exists(testcase_dir):
                os.mkdir(testcase_dir)

            testcase_path = os.path.join(testcase_dir, f"{fsm_path.split('/')[-1].replace('.json', '')}_{i+1}.json")
            with open(testcase_path, 'w', encoding='utf-8') as f_out:
                f_out.write(testcase)

            # A. Attach Testbed file
            testbed = None
            if testbed_path:
                testbed = open(testbed_path, "r").read()
                testbed_path = f"{testcase_dir}/testbed.json"
                with open(testbed_path, 'w', encoding='utf-8') as f_out:
                    f_out.write(testbed)

            generator = NaiveTestCaseGenerator()

            # 4. Generate cfg.json configuration file based on examples
            cfg = generator.few_shot_of_cfg_file(few_shot_example_cfg_path, cfg_example_path, cfg_template_path, topo_path, testcase)
            cfg_path = f"{testcase_dir}/cfg.json"
            with open(cfg_path, 'w', encoding='utf-8') as f_out:
                f_out.write(cfg)

            # 5. Generate DUT configuration files (Setup and Teardown) based on examples
            if testbed:
                testbed_json = json.loads(testbed)
                cfg_json = json.loads(cfg)
                for device_name in cfg_json['dut']:
                    device_type = testbed_json['dut'][device_name]['dut_type']
                    # Generate Setup configuration file
                    setup_cfg = generator.few_shot_of_dut_cfg(cfg_dut_testcase_example_path, cfg_example_path, cfg_dut_setup_example_path, cfg_path, topo_path, testcase, device_type, 'Setup')
                    setup_cfg_path = f"{testcase_dir}/{device_name}_Setup.txt"
                    with open(setup_cfg_path, 'w', encoding='utf-8') as f_out:
                        f_out.write(setup_cfg)
                    # Generate Teardown configuration file
                    teardown_cfg = generator.few_shot_of_dut_cfg(cfg_dut_testcase_example_path, cfg_example_path, cfg_dut_teardown_example_path, cfg_path, topo_path, testcase, device_type, 'Teardown')
                    teardown_cfg_path = f"{testcase_dir}/{device_name}_Teardown.txt"
                    with open(teardown_cfg_path, 'w', encoding='utf-8') as f_out:
                        f_out.write(teardown_cfg)
            
            logger.info(f"Test case {i+1} generated: {testcase_path}")
    else:
        pass

def generate_test_points_from_field(field_path, rfc_file_path, current_time, model="qwen-max-latest", use_content_table=False):
    """
    Extract header constraints from field file and generate test points, aiming for quantifiable coverage
    Args:
        field_path (str): Path to field file containing ASCII description of fields and context
        rfc_file_path (str): Path to RFC file
        current_time (str): Current timestamp
        model (str): Model name
        use_content_table (bool): Whether to use RFC table of contents
    Returns:
        field_json_path (str): Path to extracted header constraints JSON file
    """

    if use_content_table:
        rfc_root = build_rfc_tree(rfc_file_path.replace('.txt', '_purified.txt'))

    # Header extraction
    field_template_path="data/templates/rfc_fields/rfc_field_template.json"

    # Field extraction
    generator = TestCaseGenFromField(model=model)
    header_json = json.loads(generator.extract_packet_fields(field_path, field_template_path))
    logger.info(f"Header fields: {header_json}")

    # Save extracted Header fields JSON to same directory as header_path
    header_json_path = os.path.join(os.path.dirname(field_path), f"{os.path.basename(field_path).replace('.txt', '')}_header.json")
    with open(header_json_path, 'w', encoding='utf-8') as f_out:
        f_out.write(json.dumps(header_json, indent=2, ensure_ascii=False))
    # with open(header_json_path.replace('.json', ' copy.json'), 'w', encoding='utf-8') as f_out:
    #     f_out.write(json.dumps(header_json, indent=2, ensure_ascii=False))
    logger.info(f"Header fields JSON saved: {header_json_path}")

    # Reference extraction
    section_refs = json.loads(generator.get_refs(field_path))
    logger.info(f"Header references: {section_refs}")

    if use_content_table:
    # Supplement header_json constraints based on references
        for section in section_refs:
            header_page_content = rfc_root.get_subnode_by_id(section).get_full_page()
            header_json = json.loads(generator.extract_constraints(header_json_path, header_page_content, field_template_path))
            logger.info(f"Header constraints (update by section {section}): {header_json}")
            # Save extracted Header fields JSON to same directory as header_path
            with open(header_json_path, 'w', encoding='utf-8') as f_out:
                f_out.write(json.dumps(header_json, indent=2, ensure_ascii=False))
            logger.info(f"Header fields JSON updated: {header_json_path}")

        logger.info(f"Header fields JSON update completed.")

    return header_json_path

def generate_test_cases_from_field_constraints(field_json_path, field_path, current_time, model="qwen-max-latest", topo_path=None, testbed_path=None, std_path=None):
    """
    Generate test cases from extracted field constraints, aiming for quantifiable coverage
    """
    testcase_template_path="data/templates/test_cases/testcase_template_with_topology.json"  
    testcase_example_with_topo_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/few_shot_of_testcase_with_topo_one_6_7_6.json"
    if std_path:
          testcase_example_with_topo_path=std_path
    # Configuration generation
    few_shot_example_cfg_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/few_shot_of_testcase_with_topo_one_6_7_6.json"
    cfg_example_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/cfg.json"
    cfg_template_path="data/testcases/examples/one-tester-one-dut/cfg_template.json"
    # DUT configuration generation
    cfg_dut_testcase_example_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/few_shot_of_testcase_with_topo_one_6_7_6.json"
    cfg_dut_setup_example_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/dut_config/DeviceA_Setup.txt"
    cfg_dut_teardown_example_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/dut_config/DeviceA_Teardown.txt"


    field_json = load_json(field_json_path)
    protocol_field = field_json["protocol_field"]
    field_name = protocol_field["name"]
    protocol_fields = protocol_field["fields"]

    # Output folder under /results, create folder with current time, output filename as input_file+section (combine last two folder levels from field_json_path)   
    if not os.path.exists("results"):
        os.mkdir("results")
    output_dir = f"results/{current_time}_{model}_{field_json_path.split('/')[-3]}_Packet_fields/{field_json_path.split('/')[-2]}_{field_name.replace(' ', '_')}"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    logger.info(f"Output directory: {output_dir}")

    for field in protocol_fields: 
        # Generate test cases: organize folders by header fields
        output_dir_field = os.path.join(output_dir, field["name"].replace(' ', '_'))
        if not os.path.exists(output_dir_field):
            os.mkdir(output_dir_field)

        field_name = field["name"]
        field_desc = field["description"]
        logger.info(f"Processing field: {field_name}")
        packet_field_str = f"Packet Name: {field_name}\nField Name: {field_name}\nField Description: {field_desc}\nConstraints:\n"
        for constraint in field["constraints"]:
            packet_field_str += f"- {constraint}\n"
        
        logger.info(f"Packet field string: {packet_field_str}")

        generator = TestCaseGenFromField(model=model)
        testcases = generator.field2testcase(testcase_example_with_topo_path, field_path, packet_field_str, testcase_template_path)
        logger.info(f"Test cases: {testcases}")

        # Output test cases as testcase.json
        testcases_path = os.path.join(output_dir_field, "testcases.json")
        with open(testcases_path, 'w', encoding='utf-8') as f_out:
            f_out.write(testcases)
        logger.info(f"Test cases saved: {testcases_path}")

        # # A. Attach Testbed file
        # testbed = None
        # if testbed_path:
        #     testbed = open(testbed_path, "r").read()
        #     testbed_path = os.path.join(output_dir_field, "testbed.json")
        #     with open(testbed_path, 'w', encoding='utf-8') as f_out:
        #         f_out.write(testbed)
        #     logger.info(f"Testbed file saved: {testbed_path}")
        # # 4. Generate cfg.json configuration file based on examples
        # cfg = generator.few_shot_of_cfg_file(few_shot_example_cfg_path, cfg_example_path, cfg_template_path, None, testcases)
        # cfg_path = os.path.join(output_dir_field, "cfg.json")
        # with open(cfg_path, 'w', encoding='utf-8') as f_out:
        #     f_out.write(cfg)
        # logger.info(f"CFG file saved: {cfg_path}")
        # # 5. Generate DUT configuration files (Setup and Teardown)
        # if testbed:
        #     pass




def generate_test_cases_from_field(field_path, rfc_file_path, current_time, model="qwen-max-latest", topo_path=None, testbed_path=None, use_content_table=False, std_path=None):
    """
    Generate test cases from field file, aiming for quantifiable coverage
    Args:
        field_path (str): Path to field file containing ASCII description of fields and context
        rfc_file_path (str): Path to RFC file
        current_time (str): Current timestamp
        model (str): Model name
        topo_path (str): Path to topology file
        testbed_path (str): Path to testbed file
    Returns:
        None
    """

    # ##### 1. Analyze header fields and extract constraints #####
    field_json_path = generate_test_points_from_field(field_path, rfc_file_path, current_time, model=model, use_content_table=use_content_table)

    # header_json_path = "data/parsed_documents/RFC_headers/rfc2328/A.3.1/text_header.json.bak"

    # ##### 2. Generate test cases #####
    # if os.path.isdir(header_json_path):
    #     for root, dirs, files in os.walk(header_path):
    #         for file in files:
    #             if file == "text_header.json":
    #                 json_path = os.path.join(root, file)
    #                 header_file_path = json_path.replace('text_header.json', 'text.txt')
    #                 with open(json_path, 'r') as f:
    #                     header_json = json.load(f)
    #                 logger.info(f"Loaded header from {json_path}:\n{header_json}")

    #                 fields = header_json['protocol_header']['fields']
    #                 for field in fields:
    #                     field_name = field['name']
    #                     logger.info(f"Field Name: {field_name}")
    #                 logger.info(len(fields))
    #                 # Generate test cases
    #                 testcases = generate_test_cases_from_header_constraints(json_path, header_file_path, current_time, model=model, topo_path=topo_path, testbed_path=testbed_path)
    # Generate test cases
    testcases = generate_test_cases_from_field_constraints(field_json_path, field_path, current_time, model=model, topo_path=topo_path, testbed_path=testbed_path, std_path=std_path)



    # test_points_json = generate_test_cases_from_header_constraints(header_json_path, header_path, current_time, model=model, topo_path=topo_path, testbed_path=testbed_path)
    



def generate_test_cases_from_std(std_path, rfc_file_path, current_time, model="qwen-max-latest", topo_path=None, testbed_path=None):
    """
    Generate test cases from national/industry standards, aiming to improve coverage
    Args:
        std_path (str): Path to national/industry standard file
        rfc_file_path (str): Path to RFC file
        current_time (str): Current timestamp
        model (str): Model name
        topo_path (str): Path to topology file
        testbed_path (str): Path to testbed file
    Returns:
        None
    """

    # Case without topology constraints
    few_shot_examples_path="data/testcases/examples/few_shot_of_testcases_with_topology.json"
    testcase_template_path="data/testcases/examples/testcase_template_with_topology.json"    
    # Case with topology constraints
    few_shot_example_wo_topo_path="data/testcases/examples/one-tester-one-dut/few_shot_of_testcases_without_topology.json"
    testcase_template_wo_topo_path="data/testcases/examples/one-tester-one-dut/testcase_template_without_topology.json"
    # Configuration generation
    few_shot_example_cfg_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/few_shot_of_testcase_with_topo_one_6_7_6.json"
    cfg_example_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/cfg.json"
    cfg_template_path="data/testcases/examples/one-tester-one-dut/cfg_template.json"
    # DUT configuration generation
    cfg_dut_testcase_example_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/few_shot_of_testcase_with_topo_one_6_7_6.json"
    cfg_dut_setup_example_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/dut_config/DeviceA_Setup.txt"
    cfg_dut_teardown_example_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/dut_config/DeviceA_Teardown.txt"

    # RFC document preprocessing
    if not os.path.exists(rfc_file_path.replace('.txt', '_purified.txt')):
        purify_rfc(rfc_file_path, None)   # None defaults to generating _purified.txt file

    # Build RFC tree
    rfc_root = build_rfc_tree(rfc_file_path.replace('.txt', '_purified.txt'))

    generator = TestCaseGenFromStd(model=model)
    cfg_generator = NaiveTestCaseGenerator(model=model)

    # Get related section numbers from national/industry standard file
    rfc_content_table = rfc_root.get_subtree_content_table()
    related_sections = json.loads(generator.get_content_id(std_path, rfc_content_table))
    logger.info(f"Related sections: {related_sections}")

    # Output folder under /results, create folder with current time, output filename as input_file+section    
    if not os.path.exists("results"):
        os.mkdir("results")
    output_dir = f"results/{current_time}_{model}_{std_path.split('/')[-1].replace('.json', '')}_{rfc_file_path.split('/')[-1].replace('.txt', '')}"
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # Iteratively generate test cases
    test_cases = {"test_cases": []}
    for related_section in related_sections:
        # Generate test cases
        _test_cases = json.loads(generator.std2testcase(rfc_root, related_section, std_path, testcase_template_wo_topo_path, topo_path))
        if not _test_cases:
            logger.error(f"Test case generation failed for section {related_section}")
            continue
        test_cases["test_cases"].extend(_test_cases["test_cases"])
        logger.info(f"Test cases for section {related_section}: {_test_cases}")


        _test_cases_dir = os.path.join(output_dir, f"testcase_{related_section}")
        if not os.path.exists(_test_cases_dir):
            os.mkdir(_test_cases_dir)
        for _test_case in _test_cases["test_cases"]:
            # Generate test case file
            _test_case_dir = os.path.join(_test_cases_dir, _test_case["id"])
            if not os.path.exists(_test_case_dir):
                os.mkdir(_test_case_dir)
            _test_case_path = os.path.join(_test_case_dir, f"{std_path.split('/')[-1].replace('.json', '')}_{related_section}_{_test_case['id']}.json")
            with open(_test_case_path, 'w', encoding='utf-8') as f_out:
                f_out.write(json.dumps(_test_case, indent=2, ensure_ascii=False))
            logger.info(f"Test case file generated: {_test_case_path}")

            # A. Attach Testbed file
            testbed = None
            if testbed_path:
                testbed = open(testbed_path, "r").read()
                testbed_path = f"{_test_case_dir}/testbed.json"
                with open(testbed_path, 'w', encoding='utf-8') as f_out:
                    f_out.write(testbed)
            # 4. Generate cfg.json configuration file based on examples
            cfg = cfg_generator.few_shot_of_cfg_file(few_shot_example_cfg_path, cfg_example_path, cfg_template_path, topo_path, json.dumps(_test_case, indent=2, ensure_ascii=False))
            cfg_path = f"{_test_case_dir}/cfg.json"
            with open(cfg_path, 'w', encoding='utf-8') as f_out:
                f_out.write(cfg)
            # 5. Generate DUT configuration files (Setup and Teardown)
            if testbed:
                testbed_json = json.loads(testbed)
                cfg_json = json.loads(cfg)
                for device_name in cfg_json['dut']:
                    device_type = testbed_json['dut'][device_name]['dut_type']
                    # Generate Setup configuration file
                    setup_cfg = cfg_generator.few_shot_of_dut_cfg(cfg_dut_testcase_example_path, cfg_example_path, cfg_dut_setup_example_path, cfg_path, topo_path, json.dumps(_test_case, indent=2, ensure_ascii=False), device_type, 'Setup')
                    setup_cfg_path = f"{_test_case_dir}/{device_name}_Setup.txt"
                    with open(setup_cfg_path, 'w', encoding='utf-8') as f_out:
                        f_out.write(setup_cfg)
                    # Generate Teardown configuration file
                    teardown_cfg = cfg_generator.few_shot_of_dut_cfg(cfg_dut_testcase_example_path, cfg_example_path, cfg_dut_teardown_example_path, cfg_path, topo_path, json.dumps(_test_case, indent=2, ensure_ascii=False), device_type, 'Teardown')
                    teardown_cfg_path = f"{_test_case_dir}/{device_name}_Teardown.txt"
                    with open(teardown_cfg_path, 'w', encoding='utf-8') as f_out:
                        f_out.write(teardown_cfg)
            # exit()
        
        # # Generate test case file
        # test_cases_dir = os.path.join(output_dir, f"testcase_{related_section}")
        # if not os.path.exists(test_cases_dir):
        #     os.mkdir(test_cases_dir)
        # test_cases_path = os.path.join(test_cases_dir, f"{std_path.split('/')[-1].replace('.txt', '')}_{related_section}.json")
        # with open(test_cases_path, 'w', encoding='utf-8') as f_out:
        #     f_out.write(json.dumps(_test_cases, indent=2, ensure_ascii=False))
        # logger.info(f"Test case file generated: {test_cases_path}")
        # # A. Attach Testbed file
        # testbed = None
        # if testbed_path:
        #     testbed = open(testbed_path, "r").read()
        #     testbed_path = f"{test_cases_dir}/testbed.json"
        #     with open(testbed_path, 'w', encoding='utf-8') as f_out:
        #         f_out.write(testbed)


        # # 4. Generate cfg.json configuration file based on examples
        # cfg = cfg_generator.few_shot_of_cfg_file(few_shot_example_cfg_path, cfg_example_path, cfg_template_path, topo_path, json.dumps(_test_cases, indent=2, ensure_ascii=False))

def add_cfgs(testcase_path, current_time, model="qwen-max-latest", topo_path=None, testbed_path=None):
    """
    Generate test cases from national/industry standards, aiming to improve coverage
    Args:
        testcase_path (str): Path to test case file
        current_time (str): Current timestamp
        model (str): Model name
        topo_path (str): Path to topology file
        testbed_path (str): Path to testbed file
    Returns:
        None
    """


    # Case without topology constraints
    few_shot_examples_path="data/testcases/examples/few_shot_of_testcases_with_topology.json"
    testcase_template_path="data/testcases/examples/testcase_template_with_topology.json"    
    # Case with topology constraints
    few_shot_example_wo_topo_path="data/testcases/examples/one-tester-one-dut/few_shot_of_testcases_without_topology.json"
    testcase_template_wo_topo_path="data/testcases/examples/one-tester-one-dut/testcase_template_without_topology.json"
    # Configuration generation
    few_shot_example_cfg_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/few_shot_of_testcase_with_topo_one_6_7_6.json"
    cfg_example_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/cfg.json"
    cfg_template_path="data/testcases/examples/one-tester-one-dut/cfg_template.json"
    # DUT configuration generation
    cfg_dut_testcase_example_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/few_shot_of_testcase_with_topo_one_6_7_6.json"
    cfg_dut_setup_example_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/dut_config/DeviceA_Setup.txt"
    cfg_dut_teardown_example_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/dut_config/DeviceA_Teardown.txt"

    # Output folder in same directory as testcase_path, create separate folder for each testcase to store the testcase and related files
    output_dir = os.path.dirname(testcase_path)
    logger.info(output_dir)
    
    test_cases = json.load(open(testcase_path, 'r', encoding='utf-8'))


    for _test_case in test_cases["test_cases"]:
        # Generate test case file
        _test_case_dir = os.path.join(output_dir, _test_case["id"])
        logger.info(f"Test case dir: {_test_case_dir}")
        if not os.path.exists(_test_case_dir):
            os.mkdir(_test_case_dir)
        _test_case_path = os.path.join(_test_case_dir, f"{testcase_path.split('/')[-1].replace('.json', '')}_{_test_case['id']}.json")
        with open(_test_case_path, 'w', encoding='utf-8') as f_out:
            f_out.write(json.dumps(_test_case, indent=2, ensure_ascii=False))
        logger.info(f"Test case file generated: {_test_case_path}")

        cfg_generator = NaiveTestCaseGenerator(model=model)

        # A. Attach Testbed file
        testbed = None
        if testbed_path:
            testbed = open(testbed_path, "r").read()
            testbed_path = f"{_test_case_dir}/testbed.json"
            with open(testbed_path, 'w', encoding='utf-8') as f_out:
                f_out.write(testbed)
        # 4. Generate cfg.json configuration file based on examples
        cfg = cfg_generator.few_shot_of_cfg_file(few_shot_example_cfg_path, cfg_example_path, cfg_template_path, topo_path, json.dumps(_test_case, indent=2, ensure_ascii=False))
        cfg_path = f"{_test_case_dir}/cfg.json"
        with open(cfg_path, 'w', encoding='utf-8') as f_out:
            f_out.write(cfg)
        # 5. Generate DUT configuration files (Setup and Teardown)
        if testbed:
            testbed_json = json.loads(testbed)
            cfg_json = json.loads(cfg)
            for device_name in cfg_json['dut']:
                try:
                    device_type = testbed_json['dut'][device_name]['dut_type']
                except KeyError:
                    logger.error(f"Device {device_name} not found in testbed file.")
                    continue
                # Generate Setup configuration file
                setup_cfg = cfg_generator.few_shot_of_dut_cfg(cfg_dut_testcase_example_path, cfg_example_path, cfg_dut_setup_example_path, cfg_path, topo_path, json.dumps(_test_case, indent=2, ensure_ascii=False), device_type, 'Setup')
                setup_cfg_path = f"{_test_case_dir}/{device_name}_Setup.txt"
                with open(setup_cfg_path, 'w', encoding='utf-8') as f_out:
                    f_out.write(setup_cfg)
                # Generate Teardown configuration file
                teardown_cfg = cfg_generator.few_shot_of_dut_cfg(cfg_dut_testcase_example_path, cfg_example_path, cfg_dut_teardown_example_path, cfg_path, topo_path, json.dumps(_test_case, indent=2, ensure_ascii=False), device_type, 'Teardown')
                teardown_cfg_path = f"{_test_case_dir}/{device_name}_Teardown.txt"
                with open(teardown_cfg_path, 'w', encoding='utf-8') as f_out:
                    f_out.write(teardown_cfg)


def translate(testcase_path, current_time, model="qwen-max-latest"):
    """
    Translate test cases to English
    Args:
        testcase_path (str): Path to test case file
        current_time (str): Current timestamp
        model (str): Model name
    Returns:
        None
    """

    rfc = testcase_path.split('/')[-1].split('_')[-3]

    if not os.path.exists("results"):
        os.mkdir("results")
    output_dir = testcase_path+'_en'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    logger.info(f"Output directory: {output_dir}")

    # Traverse all testcases.json under output_dir
    
    testcases_json_paths = os.walk(testcase_path)

    translator = TestCaseTranslator(model=model)

    for root, dirs, files in testcases_json_paths:
        for file in files:
            if file == "testcases.json":
                section_name = root.split('/')[-2]
                field_name = root.split('/')[-1]
                _output_dir = os.path.join(output_dir, section_name)
                if not os.path.exists(_output_dir):
                    os.mkdir(_output_dir)
                _output_filename = field_name + '.json'
                _output_path = os.path.join(_output_dir, _output_filename)
                logger.info(f"Output path: {_output_path}")

                # Read testcases.json
                json_path = os.path.join(root, file)

                translated_testcases = translator.translate_testcase(json_path)
                
                translated_testcases_json = json.loads(translated_testcases)

                for i, testcase in enumerate(translated_testcases_json['test_cases']):
                    testcase['id'] = f"{section_name}_{field_name}_{i+1}"

                # Save translated test cases
                with open(_output_path, 'w', encoding='utf-8') as f_out:
                    f_out.write(json.dumps(translated_testcases_json, indent=2, ensure_ascii=False))
                logger.info(f"Translated test cases saved: {_output_path}")
                # exit()
                
def format_testcase(testcase_path, model, current_time, topo_path, testbed_path):
    """
    Format test cases
    Args:
        testcase_path (str): Path to test case file
    Returns:
        None
    """


    testcase_example_with_topo_path="data/testcases/examples/one-tester-one-dut/tc_6_7_6/few_shot_of_testcase_with_topo_one_6_7_6.json"
    testcase_template_path="data/testcases/examples/testcase_template_with_topology.json"

    generator = TestcaseFormator(model=model)

    testcase_json_str = generator.format_testcase(testcase_path, topo_path, testcase_template_path, testcase_example_with_topo_path)

    # Output folder under /results, create folder with current time, output filename as input_file+section    
    if not os.path.exists("results"):
        os.mkdir("results")
    output_dir = f"results/{current_time}_{model}_{testcase_path.split('/')[-1].replace('.json', '')}"
    
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # Output test case file
    testcase_name = testcase_path.split('/')[-1].replace('.txt', '.json')
    testcase_path_out = os.path.join(output_dir, testcase_name)
    with open(testcase_path_out, 'w', encoding='utf-8') as f_out:
        f_out.write(testcase_json_str)

    return testcase_path_out