CURRENT_TIME=$(date +"%Y%m%d-%H%M%S")   

# nohup python main.py \
#     --rfc-file /root/NetAutoTest/data/raw_documents/RFCs/rfc2328.txt \
#     --section 9.5 \
#     > ${CURRENT_TIME}.log 2>&1 &

# 带有拓扑约束的
# nohup python main.py \
#     --rfc-file data/raw_documents/RFCs/rfc2328.txt \
#     --section 9.5 \
#     --topo-path data/testcases/examples/one-tester-one-dut/topo_one.json \
#     --testbed-path data/testcases/examples/one-tester-one-dut/testbed_one.json \
#     > ${CURRENT_TIME}.log 2>&1 &

# 不带拓扑约束的
# nohup python main.py \
#     --rfc-file data/raw_documents/RFCs/rfc2328.txt \
#     --section 9.5 \
#     --testpoints-path data/testcases/exp_res/2025-03-12-23-07-32_qwen-max-latest_rfc2328_9.5/rfc2328_9.5_testpoints.json \
#     > ${CURRENT_TIME}.log 2>&1 &

# # 测试点生成
# nohup python main.py \
#     --rfc-file data/raw_documents/RFCs/rfc2328.txt \
#     --section 9.5 \
#     > ${CURRENT_TIME}.log 2>&1 &

# # 从 FSM path 生成
# nohup python main_cg.py \
#     --method fsm \
#     --rfc-file /root/NetAutoTest/data/parsed_documents/RFC_FSMs/rfc_2328_10.1/rfc_2328_10.1.txt \
#     --fsm-path-path /root/NetAutoTest/data/parsed_documents/RFC_FSMs/rfc_2328_10.1/rfc_2328_10.1_paths.json \
#     --testbed-path data/testcases/examples/one-tester-one-dut/testbed_one.json \
#     --topo-path data/testcases/examples/one-tester-one-dut/topo_one.json \
#     > ${CURRENT_TIME}.log 2>&1 &

# # 从 Header path 生成
# nohup python main_cg.py \
#     --method header \
#     --rfc-file data/raw_documents/RFCs/rfc2328.txt \
#     --header-file data/parsed_documents/RFC_headers/rfc2328/A.3.1/text.txt \
#     --testbed-path data/testcases/examples/one-tester-one-dut/testbed_one.json \
#     --topo-path data/testcases/examples/one-tester-one-dut/topo_one.json \
#     > ${CURRENT_TIME}.log 2>&1 &

# 从 Header path 生成
# nohup python main_cg.py \
#     --method header \
#     --rfc-file data/raw_documents/RFCs/rfc2328.txt \
#     --header-file data/parsed_documents/RFC_headers/rfc2328 \
#     --testbed-path data/testcases/examples/one-tester-one-dut/testbed_one.json \
#     --topo-path data/testcases/examples/one-tester-one-dut/topo_one.json \
#     > ${CURRENT_TIME}.log 2>&1 &

    # --use-content-table \

# 为已有测试用例补充配置文件
nohup python main_cg.py \
    --method addcfgs \
    --rfc-file data/raw_documents/RFCs/rfc2328.txt \
    --testcase-path results/2025-04-09-23-25-28_qwen-max-latest_rfc2328_Packet_Headers/A.3.2_OSPF_Hello_Packet/Options/testcases.json \
    --testbed-path data/testcases/examples/one-tester-one-dut/testbed_one.json \
    --topo-path data/testcases/examples/one-tester-one-dut/topo_one.json \
    > ${CURRENT_TIME}.log 2>&1 &

# # 翻译为英文
# nohup python main_cg.py \
#     --method translate \
#     --rfc-file data/raw_documents/RFCs/rfc2328.txt \
#     --testcase-path results/2025-04-09-23-25-28_qwen-max-latest_rfc2328_Packet_Headers \
#     > ${CURRENT_TIME}.log 2>&1 &
    
# # 从国标/行标生成
# nohup python main_cg.py \
#     --method std \
#     --std-file data/testcases/seeds/industry/cepri/tc_6_7_6/cepri_6_7_6_ospf.json \
#     --rfc-file data/raw_documents/RFCs/rfc2328.txt \
#     --testbed-path data/testcases/examples/one-tester-one-dut/testbed_one.json \
#     --topo-path data/testcases/examples/one-tester-one-dut/topo_one.json \
#     > ${CURRENT_TIME}.log 2>&1 &

# python test_cg.py --header-json-path data/parsed_documents/RFC_headers/rfc2328
# nohup python test_cg.py --fsm-text-path data/parsed_documents/RFC_FSMs/rfc_4271/rfc_4271.txt \
#     > ${CURRENT_TIME}.log 2>&1 &
# python test_cg.py --fsm-json-path data/parsed_documents/RFC_FSMs/rfc_4271/test.json
# python test_cg.py --testcases-path results/2025-04-09-23-25-28_qwen-max-latest_rfc2328_Packet_Headers_en
