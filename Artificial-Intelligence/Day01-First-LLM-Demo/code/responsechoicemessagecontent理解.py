# 这就是API返回的原始response对象
response = {
    "id": "chatcmpl-abc123xyz",
    "object": "chat.completion",
    "created": 1713456789,
    "model": "deepseek-chat",
    "choices": [
        {
            "index": 0,
            "finish_reason": "stop",
            "message": {
                "role": "assistant",
                "content": "API是应用程序编程接口，它就像餐厅里的服务员，帮你把需求传递给后厨（系统），再把结果端回来给你。"
            }
        },
        {
            "index": 1,
            "finish_reason": "stop",
            "message": {
                "role": "assistant",
                "content": "API是一套预先定义好的规则，让不同的软件之间可以互相沟通和交换数据。"
            }
        }
    ],
    "usage": {
        "prompt_tokens": 25,
        "completion_tokens": 35,
        "total_tokens": 60
    }
}

# response.choice

# 从response中取出choices
# 代码写法
choices = response["choices"]

# choices 现在长这样：
choices = [
    { "index": 0, "message": {...}, ... },  # 第1个回答
    { "index": 1, "message": {...}, ... }   # 第2个回答
]

print(choices)  # 打印出来是一个列表，里面有2个回答选项
print(len(choices))  # 输出: 2（因为模型给了2个不同的回答）

# response.choice[0]

# 从choices中取出第一个choice
# 代码写法
first_choice = choices[0]  # 或者直接 response["choices"][0]

# first_choice 现在长这样：
first_choice = {
    "index": 0,
    "finish_reason": "stop",
    "message": {
        "role": "assistant",
        "content": "API是应用程序编程接口，它就像餐厅里的服务员，帮你把需求传递给后厨（系统），再把结果端回来给你。"
    }
}

print(first_choice["index"])      # 输出: 0
print(first_choice["finish_reason"])  # 输出: stop

# response.choice[0].message

# 从第一个choice中取出message
# 代码写法
message = first_choice["message"]  # 或者 response["choices"][0]["message"]

# message 现在长这样：
message = {
    "role": "assistant",
    "content": "API是应用程序编程接口，它就像餐厅里的服务员，帮你把需求传递给后厨（系统），再把结果端回来给你。"
}

print(message["role"])    # 输出: assistant（这句话是谁说的）
print(message["content"]) # 输出: API是应用程序编程接口...

# response.choice[0].message.content

# 从第一个message中取出content(最终回答)
# 代码写法
final_answer = message["content"]  # 或者 response["choices"][0]["message"]["content"]

# final_answer 现在长这样（就是普通的字符串）：
final_answer = "API是应用程序编程接口，它就像餐厅里的服务员，帮你把需求传递给后厨（系统），再把结果端回来给你。"

print(final_answer)  # 输出最终的文本答案
print(type(final_answer))  # 输出: <class 'str'>