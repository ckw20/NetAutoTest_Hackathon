from example_builder import load_examples_from_json
from example_retriever import ExampleRetriever
from task_decomposer import load_config, build_few_shot_prompt, llm




def intent_rewrite(query_intent,config_path):
    
    config = load_config(config_path)
    examples = load_examples_from_json(config)
    retriever = ExampleRetriever(examples, config)
    top_examples = retriever.retrieve(query_intent, top_k=config["top_k"])
    prompt = build_few_shot_prompt(top_examples,config)

    content, prompt =llm(config["model"], prompt + "\nInput:\n" + query_intent,
        config["api_key"], config["base_url"])

    return content, prompt



if __name__ == "__main__":
    config_path = "/root/NetAutoTest/src/script_generator/intent_rewrite/prompts/rewrite_config.yaml"
    
    # query_intent = """
    # # =================================================================================
    # # Objective    :   测试目的 :  开放式最短路径优先路由协议（OSPF)
    # #
    # # Step         :   测试步骤1: tester port1 IP地址为192.168.1.100/24，port2为192.168.2.100/24；
    # #                   测试步骤2: DUT port1 IP地址为192.168.1.1/24，port2为 192.168.2.1/24；
    # #                   测试步骤3: 在DUT上配置OSPFv2路由协议；
    # #                   测试步骤4: 测试仪tester使用port1、port2建立OSPF路由器，在port1插入一些LSA，
    # #                              并使port1和DUT的port1达到FULL状态，port2和DUT的port2达到FULL状态，
    # #                              观察port2是否能得到port1的LSA。
    # #
    # # Criteria     :   预期结果1: ospf建立成功，可以收到lsa
    # # =================================================================================
    # """

    query_intent="""
    =================================================================================
    Objective     : Objective: 6.4.3 Port Throughput
    
    Step          : Test Step 1: According to RFC 2544, connect any two ports of the same type on the switch to the tester, as shown in Figure 3;
                    Test Step 2: Configure the traffic generator: test frame lengths are (64, 65, 256, 1024, 1518 bytes;             
                    Test Step 3: Test duration is 60 seconds.
    Criteria      : Expected Result 1: The technical requirement for throughput is 100%.
    reated by     : Tester-001
    Tags          : performance
    =================================================================================
    """
    content, prompt=intent_rewrite(query_intent,config_path)
    print("==== LLM prompt ====")
    print(prompt)
    print("==== LLM Output ====")
    print(content)
