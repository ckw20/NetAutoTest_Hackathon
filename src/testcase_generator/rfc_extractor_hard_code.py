##### v1: deepseek-v3 with text-fig #####
# from graphviz import Digraph

# # 创建一个有向图
# dot = Digraph(comment='Neighbor State Changes (Hello Protocol)')

# # 添加节点
# dot.node('Init', 'Init')
# dot.node('Attempt', 'Attempt')
# dot.node('2-Way', '2-Way')
# dot.node('ExStart', 'ExStart')
# dot.node('1-Way', '1-Way')
# dot.node('Down', 'Down')

# # 添加边
# dot.edge('Down', 'Init', label='Start')
# dot.edge('Init', 'Attempt', label='Hello Received')
# dot.edge('Attempt', 'Init', label='HelloReceived')
# dot.edge('Init', '2-Way', label='2-Way Received')
# dot.edge('Init', '1-Way', label='1-Way Received')
# dot.edge('2-Way', 'ExStart', label='ExStart')
# dot.edge('ExStart', '2-Way', label='2-Way')

# # 渲染图形
# dot.render('neighbor_state_changes', format='png', view=False)

##### v2: deepseek-v3 with fig #####

# from graphviz import Digraph

# # 创建一个有向图
# dot = Digraph(comment='State Machine')

# # 添加状态节点
# dot.node('Down', 'Down')
# dot.node('Start', 'Start')
# dot.node('HelloReceived', 'Hello Received')
# dot.node('Init', 'Init')
# dot.node('TwoWayReceived', '2-Way Received')
# dot.node('OneWayReceived', '1-Way Received')
# dot.node('ExStart', 'ExStart')

# # 添加状态之间的转换边
# dot.edge('Down', 'Start')
# dot.edge('Start', 'Attempt')
# dot.edge('HelloReceived', 'HelloReceived')
# dot.edge('Init', 'TwoWayReceived')
# dot.edge('Init', 'OneWayReceived')
# dot.edge('ExStart', 'TwoWayReceived')

# # 渲染并保存状态机图
# dot.render('state_machine', view=False)


##### v3: gpt-4o with fig #####
# from graphviz import Digraph

# def draw_state_machine():
#     dot = Digraph(comment='State Machine')

#     # 定义节点
#     states = ['Down', 'Start', 'Attempt', 'HelloReceived', 'Init', '2-Way', '1-Way', 'ExStart']
#     for state in states:
#         dot.node(state)

#     # 定义状态转移
#     # dot.edges(['DownStart', 'StartAttempt', 'StartHelloReceived', 'HelloReceivedInit', 'Init2-Way', 'Init1-Way', '2-WayExStart'])
#     dot.edges([
#         ('Down', 'Start'),
#         ('Start', 'Attempt'),
#         ('Start', 'HelloReceived'),
#         ('HelloReceived', 'Init'),
#         ('Init', '2-Way'),
#         ('Init', '1-Way'),
#         ('2-Way', 'ExStart')
#     ])

#     # 标注特殊转移
#     dot.edge('Attempt', 'HelloReceived', label='HelloReceived')
#     dot.edge('HelloReceived', 'Init', label='Hello Received')
#     dot.edge('2-Way', 'ExStart', label='ExStart')
#     dot.edge('Init', '2-Way', label='2-Way Received')
#     dot.edge('Init', '1-Way', label='1-Way Received')

#     # 输出图像
#     dot.render('state_machine', format='png', cleanup=True, view=False)

# if __name__ == "__main__":
#     draw_state_machine()

##### v4: Deepseek-3 with text-fig and text-desc #####
# from graphviz import Digraph

# # Define the states and transitions
# states = ['Down', 'Attempt', 'Init', '2-Way', 'ExStart', 'Exchange', 'Loading', 'Full']
# transitions = [
#     ('Down', 'Attempt', 'Start'),
#     ('Down', 'Init', 'HelloReceived'),
#     ('Attempt', 'Init', 'HelloReceived'),
#     ('Init', '2-Way', '2-WayReceived'),
#     ('Init', 'Init', '1-WayReceived'),
#     ('2-Way', 'ExStart', 'AdjOK?'),
#     ('ExStart', 'Exchange', 'NegotiationDone'),
#     ('Exchange', 'Loading', 'ExchangeDone'),
#     ('Exchange', 'Full', 'ExchangeDone'),
#     ('Loading', 'Full', 'LoadingDone'),
#     ('Full', 'Down', 'KillNbr, InactivityTimer, LLDown'),
#     ('ExStart', 'ExStart', 'SeqNumberMismatch, BadLSReq'),
#     ('Exchange', 'ExStart', 'SeqNumberMismatch, BadLSReq'),
#     ('Loading', 'ExStart', 'SeqNumberMismatch, BadLSReq'),
#     ('Full', 'ExStart', 'SeqNumberMismatch, BadLSReq')
# ]

# # Create a directed graph
# dot = Digraph(comment='OSPF Neighbor State Machine')

# # Add states to the graph
# for state in states:
#     dot.node(state)

# # Add transitions to the graph
# for transition in transitions:
#     dot.edge(transition[0], transition[1], label=transition[2])

# # Render the graph
# dot.render('ospf_neighbor_state_machine', format='png', cleanup=True)

# # Display the graph
# dot.view()

#####  v5: Deepseek-3 with fig and desc (10. -> 10.3.) #####
# from graphviz import Digraph

# # 创建一个有向图
# dot = Digraph(comment='OSPF Neighbor State Machine')

# # 添加状态节点
# dot.node('Down', 'Down')
# dot.node('Attempt', 'Attempt')
# dot.node('Init', 'Init')
# dot.node('2-Way', '2-Way')
# dot.node('ExStart', 'ExStart')
# dot.node('Exchange', 'Exchange')
# dot.node('Loading', 'Loading')
# dot.node('Full', 'Full')

# # 添加状态转换边（Hello Protocol）
# dot.edge('Down', 'Attempt', label='Start')
# dot.edge('Attempt', 'Init', label='HelloReceived')
# dot.edge('Down', 'Init', label='HelloReceived')
# dot.edge('Init', '2-Way', label='2-WayReceived')
# dot.edge('2-Way', 'ExStart', label='AdjOK?')

# # 添加状态转换边（Database Exchange）
# dot.edge('ExStart', 'Exchange', label='NegotiationDone')
# dot.edge('Exchange', 'Full', label='ExchangeDone')
# dot.edge('Exchange', 'Loading', label='ExchangeDone')
# dot.edge('Loading', 'Full', label='LoadingDone')

# # 添加其他事件转换边
# dot.edge('ExStart', 'ExStart', label='SeqNumberMismatch')
# dot.edge('Exchange', 'ExStart', label='SeqNumberMismatch')
# dot.edge('Loading', 'ExStart', label='SeqNumberMismatch')
# dot.edge('Full', 'ExStart', label='SeqNumberMismatch')

# dot.edge('ExStart', 'ExStart', label='BadLSReq')
# dot.edge('Exchange', 'ExStart', label='BadLSReq')
# dot.edge('Loading', 'ExStart', label='BadLSReq')
# dot.edge('Full', 'ExStart', label='BadLSReq')

# dot.edge('Any', 'Down', label='KillNbr')
# dot.edge('Any', 'Down', label='LLDown')
# dot.edge('Any', 'Down', label='InactivityTimer')

# dot.edge('2-Way', 'Init', label='1-WayReceived')
# dot.edge('ExStart', 'Init', label='1-WayReceived')
# dot.edge('Exchange', 'Init', label='1-WayReceived')
# dot.edge('Loading', 'Init', label='1-WayReceived')
# dot.edge('Full', 'Init', label='1-WayReceived')

# # 设置图形属性
# dot.attr(rankdir='LR')  # 从左到右排列状态

# # 保存并渲染图形
# dot.render('ospf_neighbor_state_machine_2', format='png', cleanup=True)



##### v6: Deepseek-r1 with fig and desc (10. -> 10.3.) #####
# from graphviz import Digraph

# # 创建Hello协议的状态转换图（图12）
# hello_graph = Digraph('OSPF Hello Protocol State Machine', format='png')
# hello_graph.attr(rankdir='LR', label='Figure 12: Neighbor state changes (Hello Protocol)')

# # 添加节点
# hello_graph.node('Down')
# hello_graph.node('Attempt')
# hello_graph.node('Init')
# hello_graph.node('2-Way')
# hello_graph.node('ExStart')

# # 添加边
# hello_graph.edge('Down', 'Attempt', label='Start')
# hello_graph.edge('Down', 'Init', label='HelloReceived')
# hello_graph.edge('Attempt', 'Init', label='HelloReceived')
# hello_graph.edge('Init', 'ExStart', label='2-WayReceived\n(Adj needed)')
# hello_graph.edge('Init', '2-Way', label='2-WayReceived\n(Adj not needed)')
# hello_graph.edge('ExStart', '2-Way', label='AdjOK?\n(Adj not needed)')
# hello_graph.edge('2-Way', 'ExStart', label='AdjOK?\n(Adj needed)')
# hello_graph.edge('Init', 'Init', label='HelloReceived', style='dashed')  # 无状态变化
# hello_graph.edge('Init', 'Down', label='1-WayReceived')
# hello_graph.edge('2-Way', 'Init', label='1-WayReceived')

# # 公共事件转换（KillNbr, LLDown, InactivityTimer）
# for state in ['Attempt', 'Init', '2-Way', 'ExStart']:
#     hello_graph.edge(state, 'Down', label='KillNbr/LLDown/InactivityTimer', color='red')

# hello_graph.render('ospf_hello_state_machine_r1', view=False, format='png')

# # 创建数据库交换的状态转换图（图13）
# db_exchange_graph = Digraph('OSPF Database Exchange State Machine', format='png')
# db_exchange_graph.attr(rankdir='LR', label='Figure 13: Neighbor state changes (Database Exchange)')

# # 添加节点
# db_exchange_graph.node('ExStart')
# db_exchange_graph.node('Exchange')
# db_exchange_graph.node('Loading')
# db_exchange_graph.node('Full')

# # 添加边
# db_exchange_graph.edge('ExStart', 'Exchange', label='NegotiationDone')
# db_exchange_graph.edge('Exchange', 'Full', label='ExchangeDone\n(LS Req empty)')
# db_exchange_graph.edge('Exchange', 'Loading', label='ExchangeDone\n(LS Req non-empty)')
# db_exchange_graph.edge('Loading', 'Full', label='LoadingDone')
# db_exchange_graph.edge('Exchange', 'ExStart', label='SeqNumberMismatch/BadLSReq', color='blue')
# db_exchange_graph.edge('Loading', 'ExStart', label='SeqNumberMismatch/BadLSReq', color='blue')
# db_exchange_graph.edge('Full', 'ExStart', label='SeqNumberMismatch/BadLSReq', color='blue')

# # 公共事件转换（KillNbr, LLDown, InactivityTimer）
# for state in ['ExStart', 'Exchange', 'Loading', 'Full']:
#     db_exchange_graph.edge(state, 'Down', label='KillNbr/LLDown/InactivityTimer', color='red')

# db_exchange_graph.render('ospf_db_exchange_state_machine_r1', view=False, format='png')



##### v7: Deepseek-r1 (table) and v3 (code) #####
# from graphviz import Digraph

# # Create Figure 12: Neighbor state changes (Hello Protocol)
# dot_12 = Digraph(comment='OSPF Neighbor State Machine (Hello Protocol)')

# # Add states
# dot_12.node('Down', 'Down')
# dot_12.node('Attempt', 'Attempt')
# dot_12.node('Init', 'Init')
# dot_12.node('2-Way', '2-Way')

# # Add transitions
# dot_12.edge('Down', 'Attempt', label='Start')
# dot_12.edge('Down', 'Init', label='HelloReceived')
# dot_12.edge('Attempt', 'Init', label='HelloReceived')
# dot_12.edge('Init', '2-Way', label='2-WayReceived')
# dot_12.edge('2-Way', 'Init', label='1-WayReceived')

# # Render and save Figure 12
# dot_12.render('ospf_neighbor_state_machine_hello_protocol_r1_v3', format='png', cleanup=True)

# # Create Figure 13: Neighbor state changes (Database Exchange)
# dot_13 = Digraph(comment='OSPF Neighbor State Machine (Database Exchange)')

# # Add states
# dot_13.node('ExStart', 'ExStart')
# dot_13.node('Exchange', 'Exchange')
# dot_13.node('Loading', 'Loading')
# dot_13.node('Full', 'Full')

# # Add transitions
# dot_13.edge('ExStart', 'Exchange', label='NegotiationDone')
# dot_13.edge('Exchange', 'Full', label='ExchangeDone')
# dot_13.edge('Exchange', 'Loading', label='ExchangeDone')
# dot_13.edge('Loading', 'Full', label='LoadingDone')
# dot_13.edge('Exchange', 'ExStart', label='SeqNumberMismatch')
# dot_13.edge('Exchange', 'ExStart', label='BadLSReq')

# # Render and save Figure 13
# dot_13.render('ospf_neighbor_state_machine_database_exchange_r1_v3', format='png', cleanup=True)

##### v8: Deepseek-r1 (table) and v3 (code) -2 #####
from graphviz import Digraph

# 创建 Hello 协议的状态转换图
hello_graph = Digraph('Hello Protocol State Changes', format='png')
hello_graph.attr(rankdir='LR')

# 添加状态节点
hello_graph.node('Down')
hello_graph.node('Attempt')
hello_graph.node('Init')
hello_graph.node('2-Way')

# 添加状态转换边
hello_graph.edge('Down', 'Attempt', label='Start')
hello_graph.edge('Down', 'Init', label='HelloReceived')
hello_graph.edge('Attempt', 'Init', label='HelloReceived')
hello_graph.edge('Init', '2-Way', label='2-WayReceived')
hello_graph.edge('Init', 'Init', label='1-WayReceived')
hello_graph.edge('2-Way', 'Init', label='1-WayReceived')
hello_graph.edge('2-Way', '2-Way', label='2-WayReceived')
hello_graph.edge('Init', 'Init', label='HelloReceived')
hello_graph.edge('2-Way', '2-Way', label='HelloReceived')

# 保存并渲染图
hello_graph.render('hello_protocol_state_changes_r1_v3_2', view=False)

# 创建数据库交换的状态转换图
db_exchange_graph = Digraph('Database Exchange State Changes', format='png')
db_exchange_graph.attr(rankdir='LR')

# 添加状态节点
db_exchange_graph.node('ExStart')
db_exchange_graph.node('Exchange')
db_exchange_graph.node('Loading')
db_exchange_graph.node('Full')

# 添加状态转换边
db_exchange_graph.edge('ExStart', 'Exchange', label='NegotiationDone')
db_exchange_graph.edge('Exchange', 'Full', label='ExchangeDone')
db_exchange_graph.edge('Exchange', 'Loading', label='ExchangeDone')
db_exchange_graph.edge('Loading', 'Full', label='LoadingDone')
db_exchange_graph.edge('Exchange', 'ExStart', label='SeqNumberMismatch')
db_exchange_graph.edge('Exchange', 'ExStart', label='BadLSReq')
db_exchange_graph.edge('Loading', 'ExStart', label='SeqNumberMismatch')
db_exchange_graph.edge('Loading', 'ExStart', label='BadLSReq')
db_exchange_graph.edge('Full', 'ExStart', label='SeqNumberMismatch')
db_exchange_graph.edge('Full', 'ExStart', label='BadLSReq')

# 保存并渲染图
db_exchange_graph.render('db_exchange_state_changes_r1_v3_2', view=False)