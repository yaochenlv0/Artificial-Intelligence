import os
# 使用from openai import ApenAI不是只能调用openai,只是使用到里面的调用方法OpenAI()
# 真正调用谁，取决于OpenAI中的参数api_key、base_url
from openai import OpenAI

# 创建一个“调用大模型接口的客户端对象”，即调用模型的工具
client = OpenAI(
    # 获取服务商（deepseek）的凭证认证
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    # 调用请求发到服务商（deepseek）的服务器
    base_url="https://api.deepseek.com"
)
# 总结：准备一个API调用工具，调用时拿系统环境变量里的DEEPSEEK_API_KEY作为通行证，并且把调用请求发送给deepseek的服务器

# 将模型返回的结果保存到变量response中
# client 前面创建的调用API的对象（工具）
# chat 按“消息列表”的形式，将对话发送给模型
# completions 根据前面提供的上下文，让模型基于此生成回答
# create 创建一次请求
# 总结： 创建一次调用deepseekAPI接口的请求，按照“消息列表”的形式，将对话发送给大模型，并基于此生成回答
response = client.chat.completions.create(
    # 调用该服务商下的哪个模型
    model="deepseek-chat",
    # 对话采用列表形式，方便模型查看
    messages=[
        # 第一条消息，表示这是一条系统指令，告诉模型现在要以“有帮助的助手”这种方式来回答
        # 系统角色的信息，就是程序设计者预先设定的一套高优先级规则，用来约束模型的身份、风格、边界
        {"role": "system", "content": "你是一个有帮助的助手"},
        # 第二条消息，用户提问的问题
        {"role": "user", "content": "你好，请用一句话介绍一下什么是API"}
    ],
    # 不采用流式输出，等模型完整生成答案之后，一次性返回
    stream=False
)
# 总结：调用已经准备好的deepseek-chat模型的API接口，将列表信息以对话的形式发送给大模型，然后大模型基于此来生成回答，并且规定不要以流式方式生成回答

# response 模型返回的结果
# choice 将模型返回的回答，放到choice列表当中 choice[0] 表示取回答列表中的第一个回答
# message 取回答中的消息对象
# content 取这条消息里面的具体文本内容
print(response.choices[0].message.content)

"""
# 输出
D:\项目\python\人工智能\人工智能应用\.venv\Scripts\python.exe D:\项目\python\人工智能\人工智能应用\Day1：跑通第一个大模型程序\第一个大模型程序.py 
API是软件系统之间进行数据交互和功能调用的标准化接口。

进程已结束，退出代码为 0

"""
