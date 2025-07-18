# CEPRI

南网科研院-信息安全部-自动化项目

## 环境安装

### 修改pip下载源
`pip config set global.index-url https://mirrors.aliyun.com/pypi/simple`

### 保持联网项目根目录下执行
`pip install -r requirements.txt`

## 目录解析：
1. -config: 项目设置与版本管理
2. -docs: 项目相关文档
3. -command: 存放测试用例被测设备命令
4. -CustomLibrary: 项目依赖函数类库
5. -NtoLibrary: IXIA物理层设备NTO5800设备自动化控制库
6. -TestCase: 测试用例归档路径
7. -tool: 项目依赖工具目录
8. -whl: 项目依赖whl的python库包
