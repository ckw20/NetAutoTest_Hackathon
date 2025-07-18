import logging
import datetime
import os
from src.utils.logger import configure_root_logger
from src.testcase_generator import testcase_generator 
from src.testcase_generator.llm_agents import Testcase2JSON
import argparse
import json

LOG_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}


if __name__ == "__main__":  
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Generate test cases for RFC documents.")
    parser.add_argument("--method", type=str, default="fsm", help="The method to use for test case generation. Options: [rfc, fsm, field, std, addcfgs, translate, from_existing].")
    parser.add_argument("--sub-step", type=str, default=None, help="The sub-step to use for test case generation. Options: [understanding, testcase-gen].")
    parser.add_argument("-m", "--model", type=str, default="qwen-max-latest", help="The model to use for test case generation. Options: [qwen-max-latest, deepseek-v3, deepseek-r1, gpt-4o]") 
    parser.add_argument("-i", "--rfc-file", type=str, help="The input RFC file or the FSM text file to generate test cases..")
    parser.add_argument("--std-file", type=str, default=None, help="The input STD file to generate test cases.")
    parser.add_argument("--field-file", type=str, default=None, help="The input field file to generate test cases.")
    parser.add_argument("--field-json", type=str, default=None, help="The input field JSON file to generate test cases.")
    parser.add_argument("-o", "--output-testcase", type=str, default=None, help="The output testcase file path.")
    parser.add_argument("-s", "--section", type=str, default=None, help="The section to generate test cases.")
    parser.add_argument("--topo-path", type=str, default=None, help="The topology to generate test cases.")
    parser.add_argument("--testbed-path", type=str, default=None, help="The testbed to generate test cases.")
    parser.add_argument("--testpoints-path", type=str, default=None, help="The testpoint to generate test cases.")
    parser.add_argument("--testcase-path", type=str, default=None, help="The testcase path to generate cfgs.")
    parser.add_argument("--use-content-table", action="store_true",  help="Whether to use the content table in the RFC file.")

    # parser.add_argument("--fsm-rfc-text-path", type=str, default=None, help="The FSM text file to generate test cases.")
    parser.add_argument("--fsm-path-path", type=str, default=None, help="The FSM path to generate test cases.")

    parser.add_argument("-l", "--log_level", type=str, default="INFO", help="The log level: DEBUG, INFO, WARNING, ERROR, CRITICAL.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode.")
    args = parser.parse_args()


    # Create a folder with the current time to store log files
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    if not os.path.exists("logs"):
        os.mkdir("logs")

    # Initialize the logging system. The filename includes the current time, the model used, the input filename, section, etc.
    if args.rfc_file:
        configure_root_logger(
            filename=f"logs/{current_time}_{args.model}_{args.rfc_file.split('/')[-1].replace('.txt', '')}_{args.section}.log",
            level=LOG_LEVELS[args.log_level],
            format_str="[%(asctime)s] %(name)-25s %(levelname)-8s %(message)s" if args.verbose else "%(message)s"
        )
    else:
        configure_root_logger(
            filename=f"logs/{current_time}_{args.model}__{args.testcase_path.split('/')[-1].replace('.txt', '')}.log",
            level=LOG_LEVELS[args.log_level],
            format_str="[%(asctime)s] %(name)-25s %(levelname)-8s %(message)s" if args.verbose else "%(message)s"
        )


    # Get the logger object
    logger = logging.getLogger(__name__)  

    # Output all args content
    logger.info(args)

    # Preprocess the std_file and convert it to JSON format
    if args.std_file:
        generator = Testcase2JSON()
        if not os.path.exists(args.std_file.replace(".txt", ".json")):
            logger.info(f"Converting {args.std_file} to JSON format...")
            # Call the testcase2json method to convert
            std_json_str = generator.testcase2json(args.std_file)
            std_json_path = args.std_file.replace(".txt", ".json")
            with open(std_json_path, "w") as f:
                f.write(std_json_str)
        else:
            std_json_path = args.std_file.replace(".txt", ".json")
            logger.info(f"Using existing JSON file: {std_json_path}")
    

    ############################# 1. Generate test cases from RFC ############################
    if args.method == "rfc":    # Naively generate test cases directly from RFC
        testcase_generator.generate_test_cases_from_rfc(args.rfc_file, args.section, args.output_testcase, current_time, model=args.model, topo_path=args.topo_path, testpoint_path=args.testpoints_path, testbed_path=args.testbed_path)
    elif args.method == "fsm":  # Extract formatted FSM information and then generate test cases
        testcase_generator.generate_test_cases_from_fsm(args.fsm_path_path, args.rfc_file, current_time, args.model, topo_path=args.topo_path, testbed_path=args.testbed_path)
    elif args.method == "field":   # Extract formatted information from fields and then generate test cases
        # testcase_generator.generate_test_cases_from_field(args.field_file, args.rfc_file, current_time, args.model, topo_path=args.topo_path, testbed_path=args.testbed_path, use_content_table=args.use_content_table, std_path=std_json_path)
        field_json_path = args.field_json
        if not args.sub_step or args.sub_step == "understanding":
            logger.info(f"Generating field JSON from field file {args.field_file}...")
            field_json_path = testcase_generator.generate_test_points_from_field(args.field_file, args.rfc_file, current_time, model=args.model, use_content_table=args.use_content_table)
        if not args.sub_step or args.sub_step == "testcase-gen":
            logger.info(f"Generating test cases from field JSON {field_json_path}...")
            assert field_json_path, "Field JSON path must be provided for test case generation."
            testcases = testcase_generator.generate_test_cases_from_field_constraints(field_json_path, args.field_file, current_time, model=args.model, topo_path=args.topo_path, testbed_path=args.testbed_path, std_path=std_json_path)
            ######### TODO #########
    elif args.method == "std":      # Generate test cases directly from standards
        testcase_generator.generate_test_cases_from_std(args.std_file, args.rfc_file, current_time, args.model, topo_path=args.topo_path, testbed_path=args.testbed_path)
    elif args.method == "addcfgs":  # Add configurations to generated test cases
        testcase_generator.add_cfgs(args.testcase_path, current_time, args.model, topo_path=args.topo_path, testbed_path=args.testbed_path)
    elif args.method == "translate":  # Translate generated test cases
        testcase_generator.translate(testcase_path=args.testcase_path, current_time=current_time, model=args.model)
    elif args.method == "from_existing":
        testcase_json_path = testcase_generator.format_testcase(testcase_path=args.testcase_path, model=args.model, current_time=current_time, topo_path=args.topo_path, testbed_path=args.testbed_path)
        testcase_generator.add_cfgs(testcase_json_path, current_time, args.model, topo_path=args.topo_path, testbed_path=args.testbed_path)

    else:
        logger.error(f"Invalid method: {args.method}. Please choose from [rfc, fsm, field, std, addcfgs].")