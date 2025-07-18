# Intent Rewrite System

项目实现一个基于大模型的意图重写，结合示例构建、示例检索、任务分解和提示构建等模块，提升自然语言任务的理解与生成能力。适用于网络测试脚本生成等场景。

## 项目结构

| 模块名                    | 功能描述                                                                 |
|-------------------------|--------------------------------------------------------------------------|
| `historical_example_process.py`    | 历史已有示例改写构建改写示例库，与其他模块是解耦合的。       |
| `example_builder.py`    | 示例构建器：定义 `ExampleEntry` 类，提供数据清洗与加载函数，构建标准示例库。       |
| `example_retriever.py`  | 示例选择器：融合多种检索策略（Embedding + BM25 + 编辑距离 + CrossEncoder 重排），从示例集中选出最相关的示例。 |
| `task_decomposer.py`    | 任务分解器：基于意图构造提示词 prompt，与大语言模型交互生成子任务描述及中间结果。     |
| `main.py`               | 主控制模块：整合各子模块逻辑，执行完整的意图重写流程并输出结果。                     |

## 快速开始

```bash

# 运行主程序
python main.py
```

## 其它说明
1、语义嵌入目前使用的是本地开源模型 paraphrase-multilingual-MiniLM-L12-v2 ，也可以通过设置 use_remote: true 及相关参数，使用远程embedding模型，本地模型和远程模型二者选其一即可

2、精排模型也可以选择是否使用

3、最终的相似度得分是综合 Embedding 语义向量相似得分 + BM25 关键词详细得分 + 编辑距离 字符相似得分 + CrossEncoder 重排得分 所得，权重可以自由调整

4、其它文件说明：

- `example_process_config.yaml` --> `historical_example_process.py` 的配置文件  
- `prompt_example_process_*.yaml` --> `historical_example_process.py` 的提示词文件
- `rewrite_config.yaml`  --> `main.py` 的配置文件，中英文切换改为 `language: en`（默认中文）  
- `./data/rewrite_results/all_python_results_chinese.json`  --> 中文示例改写文件  
- `./data/rewrite_results/all_python_results_english.json`  --> 英文示例改写文件
