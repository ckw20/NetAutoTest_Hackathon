# NetAutoTest

使用LLM Agents实现网络设备测试自动化@Xinertel

## 主要模块介绍
- `src.doc_parser`: 文档解析
- `src.testcase_generator`: 测例生成
- `src.script_generator`: 脚本生成
- `src.validation`: 验证反馈

## Requirements
### 测例生成
```
openai=1.60.1
jsonschema==4.23.0
```
阿里云百炼大模型服务平台 API key：放入环境变量`DASHSCOPE_API_KEY=your_api_key`

### 代码生成
**特别建议手动安装 pytorch，以避免 CUDA 相关工具版本不一致的问题。详见 [PyTorch 官网](https://pytorch.org/get-started/locally/)。**

建议在 conda 中安装环境，以免环境冲突：

```shell
conda create -n test python=3.11.9
conda activate test
pip3 install -r requirments_sg_py.txt
```

或者：

```shell
conda create -n test python=3.11.9
conda activate test
conda install --file requirements_sg_conda.txt
```

## 使用方法
### 1. 测试用例生成（可选）

- 适用于从协议规范生成测试用例场景
- 从已有测例生成代码请从步骤2开始

#### 1.1 数据准备
1. 下载标准文档（例如RFC）文本，放入`data/raw_documents`文件夹。
2. 从标准问答中摘取待测试部分（例如协议包字段、有限状态机等），放入`data/parsed_documents`文件夹。
3. 选择相关行业标准/企业标准测试用例，放入`data/testcases/examples`文件夹中。参考其中对应JSON模板进行格式化处理。
#### 1.2 协议标准文档解析 + 已有测例引导的测试用例生成  [ TODO: 拆分为两部分 ]
以OSPF协议的Hello packet为例。
```bash
python main_cg.py \
    --method field \
    --rfc-file data/raw_documents/RFCs/rfc2328.txt \
    --field-file data/parsed_documents/RFC_fields/rfc2328/A.3.2/text.txt \
    --testbed-path data/testcases/examples/one-tester-one-dut/testbed_one.json \
    --std-file data/testcases/examples/one-tester-one-dut/tc_6_7_6/cepri_tc_6_7_6.txt
```
生成的协议字段解析文件位于`field-file`同目录下。
生成的测试用例位于`result`文件夹中。
##### 1.2.1 协议标准文档解析
协议Field理解:
```bash
python main_cg.py \
    --method field \
    --sub-step understanding \
    --rfc-file data/raw_documents/RFCs/rfc2328.txt \
    --field-file data/parsed_documents/RFC_fields/rfc2328/A.3.2/text.txt \
    --testbed-path data/testcases/examples/one-tester-one-dut/testbed_one.json \
    --std-file data/testcases/examples/one-tester-one-dut/tc_6_7_6/cepri_tc_6_7_6.txt
```

##### 1.2.2 从协议理解生成测试用例
协议Field测例生成:
```bash
python main_cg.py \
    --method field \
    --sub-step testcase-gen \
    --rfc-file data/raw_documents/RFCs/rfc2328.txt \
    --field-file data/parsed_documents/RFC_fields/rfc2328/A.3.2/text.txt \
    --testbed-path data/testcases/examples/one-tester-one-dut/testbed_one.json \
    --std-file data/testcases/examples/one-tester-one-dut/tc_6_7_6/cepri_tc_6_7_6.txt
```

#### 1.3 测试仪及被测设备相关配置文件生成
其中testcase-path需替换为`result`文件夹中刚才生成的某个测试用例路径。
```bash
python main_cg.py \
    --method addcfgs \
    --rfc-file data/raw_documents/RFCs/rfc2328.txt \
    --testcase-path results/2025-04-17-23-53-16_qwen-max-latest_rfc2328_Packet_fields/A.3.2_Hello_Packet/HelloInterval/testcases.json \
    --testbed-path data/testcases/examples/one-tester-one-dut/testbed_one.json \
    --topo-path data/testcases/examples/one-tester-one-dut/topo_one.json
```
生成的配置文件位于`testcase-path`的JSON文件同目录下，每个testcase生成一个独立的文件夹。配置文件的正确性需要人工检查验证。

### 2 已有测试用例的配置生成（可选）

- 适用于输入已有测试用例的情形，生成的文件包括：格式化的测试用例、被测设备配置文件、测试仪自动化脚本配置文件
- 替换待测试用例路径 `--testcase-path` 即可
- 默认在一个tester搭配一个DUT的拓扑下进行测试，若需要更换拓扑/测试床信息，请更换 `--testbed-path` 和 `--topo-path` 文件

```bash
python main_cg.py \
    --method from_existing \
    --testcase-path data/testcases/existing/tc_2_1_2_1_1.txt \
    --testbed-path data/testcases/examples/one-tester-one-dut/testbed_one.json \
    --topo-path data/testcases/examples/one-tester-one-dut/topo_one.json
```

### 3 测试代码生成

一键运行：

```shell
python main_sg.py --config /path/to/your/config
```

例如,

```shell
python main_sg.py --config ./data/run_config/2025-04-09-OSPF-001-HelloInterval-new.json
```

其中 json 文件参数含义如下：

```json
{
    "Task": {
        "dir": "存 testcase 的目录，理论上里面有任务.json, cfg.json, testbed.json, Device*_*.txt",
        "task": "任务文件名"
    },
    "API": {
        "description": "检索 API 相关参数",
        "doc": "API 文档地址",
        "specified": "由于目前不微调时检索准确率低，通过该文件指定 API",
        "Retriever": {
            "description": "检索模型参数，详见下文"
        }
    },
    "Example": {
        "Description": "用于检索示例的相关参数",
        "dir": "南网仓库结构，不用变",
        "dir_no_cfg": "文档附带示例结构，不用变；如果不想包含这个目录的示例，可以直接把这一条删掉。",
        "specified": "同 API specified",
        "Retriever": {
            "description": "检索模型参数，详见下文"
        }
    },
    "Code": {
        "system_prompt": "系统提示词位置，不用改",
        "max_iter": "最大迭代轮数，可以设大一点",
        "remove_past_assistant": "建议开启",
        "Generator": {
            "description": "用于生成代码的 LLM，遵循 OpenAI 接口",
            "api_key": "**请使用您们的 api_key**",
            "base_url": "例如 https://dashscope.aliyuncs.com/compatible-mode/v1",
            "model": "例如 qwen-max-latest"
        },
        "assistant_content": "上一次运行的 LLM 生成的代码地址，通常在 temp_script/{current_time}/iter_{iter}/main.py",
        "user_content": "上一次运行的反馈给 LLM 的信息，通常在 temp_script/{current_time}/iter_{iter}/user_content.txt",
    },
    "Experience": {
        "pool_path": "经验池地址，该文件是 list[dict]",
        "Retriever": {
            "description": "检索模型参数，详见下文"
        }
    },
    "FeedbackAgent": {
        "HL_enable": "是否启用 Human-in-the-Loop，详情见下"
    },
}
```

**请务必修改 `api_key` 这个参数，我本人的余额有限。**

## 其它相关问题

### 流程文件相关

每一轮生成并运行代码后，会在 `temp_script/{current_time}/iter_{iter}/` 下生成：

- `main.py`：生成的代码
- `response.json`：运行的结果
- `expert_exp.json`：检索到的专家经验
- `user_content.txt`：下一轮即将反馈给 LLM 的

如果不小心终止了当前的迭代（或者迭代轮数设小了），希望从半截开始生成，可以使用上面 `assistant_content` 和 `user_content` 以从半截生成。

### HL_enable

是否启用人类反馈。

若不启用，则流程是全自动的，目前默认**代码会运行直到 status = "success" 且 verdict = "pass"**，分别表示程序正常结束和 DUT 行为符合预期。

否则，每一轮流程末尾，会等待人类输入。此时可以：

- 不输入，直接 enter，会使用 `response.json` 中信息的作为 feedback
    - 除非 status = "success" 且 verdict = "pass" 
- 输入 success：表示通过 manual review，结束迭代流程并出 result
- 输入一个数字或一个列表的数字（例如 `1` 或者 `[0,2,3]`）：采用检索到的专家经验（见 `expert_exp.json`），下标从 0 开始
- 其它字符串：表示人类反馈，该反馈会被加入到经验池（`pool_path` 对应的文件）

不过，即使 status = "success" 且 verdict = "pass"，也可以输入反馈，以进行下一轮迭代。

### Retriever

三种检索（API、示例、专家经验）用的模型结构是通用的，目前支持两种：local 和 remote，完整的配置如下：

```json
{
    "Retriever": {
        "local_model_type": "SentenceTransformer 或 CrossEncoder",
        "local_model_name_or_path": "例如 multi-qa-mpnet-base-cos-v1，或使用我们微调过的模型（微调模型目录请咨询王亚文）",
        "local_BM25_enable": "是否在后续嵌入检索前先用 BM25 进行初筛；目前建议全部不启用，因为效果不好",
        "local_BM25_k": "先进行 BM25 选出多少",
        "local_embedding_k": "本地嵌入模型最终选出多少",

        
        "remote_base_url": "例如 https://dashscope.aliyuncs.com/compatible-mode/v1",
        "remote_api_key": "您的 API key",
        "remote_embedding_model": "例如 text-embedding-v3；目前默认向量长度 1024，若模型不支持可能需要暂时到代码里改一下默认参数",
        "remote_rerank_model": "例如 gte-rerank-v2",
        "remote_corpus2embedding_path": "dict, 存储此前计算过的 corpus(str) => embedding(list[float])，以避免重复计算（因为很慢）",
        "remote_embedding_k": "嵌入检索多少个",
        "remote_rerank_k": "在嵌入检索的基础上（若有）最终再重排出多少个"
    }
}
```

两种可以只启用其中一种，也可以都启用。对于后者，目前会直接把检索结果拼起来。

#### local

用小模型做嵌入/重排，目前支持 SentenceTransformer 和 CrossEncoder

关于可用模型，详见 [Sentence-Transformers 官网](https://www.sbert.net/index.html)。

现在模型精度不足，可能需要人工指定示例和 API（示例中的 API 也会被加入 prompt，但不会超过上限 k）。

未来会进行进一步微调以提升精准度，并将模型上传到某个可供下载的位置。

目前已经初步微调了一些，其效果和地址请咨询王亚文，或者自行手动微调（见根目录下的 \*finetune\*.py），强烈建议 API 检索使用本地微调模型。

#### remote

用较大的远程模型做嵌入/重排，embedding 和 rerank 需要启用至少一个。

若都启用，则会先进行 embedding，在此基础上进行 rerank。

建议示例检索同时开启，经验检索取决于经验池的规模，比较小时可以不启用 embedding。


### run_script_api & ssh_config

目前在 `main_sg.py` 里有一个 `run_script_api` 方法，其接收 `dir: str` 参数，该 `dir` 目录下会包含所有 `main.py` 和各种其它文件。

在目前的实现里，`run_script_api()` 会通过 ssh 将这些文件压缩并发送到 testbed 中的 `./temp_script/{current_time}/iter_{iter}` 文件夹底下并解压，然后运行 testbed 中的 `python response_sg.py -p ./temp_script/{current_time}/iter_{iter}`，其运行结果在该目录底下的 `response.json`。

可以直接在 testbed 上 `python response_sg.py -p ./temp_script/{current_time}/iter_{iter}` 运行代码以进行调试，其会自动把各种配置文件和下发文件放到南网仓库下的各个地方。其后也可以找到南网仓库的 `testcase/{tc_no}/main.py` 直接运行调试（不特别推荐）。

需要修改 `src/remote_utils/ssh_config.py` 中的参数，如果 ssh 相关信息发生变动：

```python
import paramiko
from .ssh_config_template import *
private_key = paramiko.RSAKey.from_private_key_file("/root/.ssh/id_rsa")
ssh_config_xrt = ssh_config_template("166.111.239.1", 2223, "xrt", private_key)
```

**更换服务器时需要配置 ssh，以使当前服务器可以无密码的访问 testbed**



## 功能实现
- 文档解析
    - ✅ API 文档形式化解析
    - ✅ API 文档 LLM 解析
    - ⏳ 差异比对与反馈纠错
- 测例生成
    - RFC 文档处理
        - ✅ RFC文档章节拆分
        - ✅ 相关章节提取
        - ⏳ 协议状态机提取
        - ⏳ RFC 知识图谱构建
    - 测试点生成
        - ✅ 基于推理模型的测试点生成
        - ✅ 拓扑限制下的测试点生成（@Demo）
        - ⏳ 基于覆盖度检测反馈的全面测试点生成
    - 测试用例生成
        - 基于LLM的测例生成
            - ✅ 拓扑自由的测例生成
            - ✅ 拓扑限制下的测例生成（@Demo）
        - ✅ 初步生成测例配置文件 cfg.json
        - ✅ 初步生成被测设备配置文件
        - ⏳ 引入搜索引擎
    - 测例评价反馈
        - ✅ 测例格式检查 (JSON schema) 
        - ⏳ 正确性评价指标构建
        - ⏳ 覆盖度评价指标构建
        - ⏳ 面向覆盖度提升的反馈迭代
    - Common
        - ⏳ LLM 的 RFC 微调（需验证泛化性）
- 脚本生成
    - 检索器
        - ✅ 解析格式化 API doc (json)
        - ✅ 稀疏检索 BM-25
        - ✅ 密集检索 RAG (SBERT)
        - ❌ 接入反馈-重新/补充/强制检索
        - ❌ 从示例代码提取相关 API
        - ❌ 接入微调代码
    - 代码生成
        - 加载测例
            - ✅ 解析格式化测例
            - ✅ 格式化测例转 prompt
            - ✅ 解析参考示例并转 prompt
            - ✅ 解析 cfg.json, testbed.json 并转 prompt
            - ❌ 提取拓扑信息并转为 prompt
        - LLM Client
           - ✅ Remote LLM Client，用于提示词工程
           - ❌ Local LLM Client，并设计微调任务
        - 接入 Feedback
            - ✅ 创建 FeedbackAgent
            - ✅ 接入用于跑通、测试的模拟反馈接口
            - ⏳ 接入语法验证：已接入接口
            - ⏳ 接入真实运行验证：已接入接口
            - ✅ 接入人工反馈
            - ⏳ 整合成 prompt：已部分整合
            - ❌ 从本地加载开始前的预设经验
        - 整体框架：整体代码生成流程
            - ✅ 实现单次迭代接口
            - ✅ 整合多轮反馈流程
    - bugs: 解决 tokens 过长的问题
        - ✅ 对示例文档也做一次 RAG
        - ✅ 只保留历史 messages 有用的信息
    - 未来工程改动
        - ❌ 引入经验池，人工反馈前自动查历史中比较相似的问题
    - 未来创新调优关注
        - ⏳ 代码生成调优
        - ⏳ 检索调优
- 验证反馈
    - ✅ 已实现
    - ⏳ TODO
    
 *(✅: 已实现; ⏳: 实现中; ❌: 未实现;)*

## 备注
- 现阶段目标：修改整合各模块，统一入口`main.py`，实现文档解析、测例生成、脚本生成全流程Demo
- `main.py` 定义了统一logger配置，模块中`import logging`，使用`logger = logging.getLogger(__name__)`即可
