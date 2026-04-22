import os
from openai import OpenAI

# 初始化客户端
# 初始化调用API的对象
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 像模型提问并返回答案
def ask_question(question):
    # 先进入try中执行程序，如果程序出错，则进入except中执行程序
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "user","content": question}
            ],
            # 控制随机性
            # 数值越低，回答越精确；数值越高，回答越天马行空，越有创造力
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"出错了：{str(e)}"

def main():
    print("="*50)
    print("简单问答程序（输入'quit'或'exit'退出）")
    print("="*50)

    # 无限循环，遇见break则中止
    while True:
        # 获取用户输入
        # strip() 去掉空格、制表符、换行符
        question = input("问题：").strip()

        # 退出条件
        # lower() 将字符串全部转换为小写
        # 忽略大小写后，如果用户输入的是quit、exit、q
        if question.lower() in ['quit', 'exit', 'q']:
            print("再见！")
            break

        # 跳过空输入
        # 如果用户输入的是空字符串
        if not question:
            print("请输入问题：")
            # 跳过本次循环剩余代码，进行下一次循环
            continue

        # 调用模型
        print("思考中...")
        answer = ask_question(question)

        # 打印答案
        print(f"答案：{answer}")

if __name__=="__main__":
    main()

"""
D:\项目\python\人工智能\人工智能应用\.venv\Scripts\python.exe D:\项目\python\人工智能\人工智能应用\Day2：做一个最简单的问答程序\最简单的问答程序.py 
==================================================
简单问答程序（输入'quit'或'exit'退出）
==================================================
问题：几点了
思考中...
答案：我无法获取实时时间，因为我是离线运行的AI助手。建议您查看手机、电脑或手表上的时间，或者询问其他在线设备（如智能音箱）。如果需要特定时区的时间，可以告诉我您所在的地区，我可以帮您估算当前时间哦！ 😊
问题：q
再见！

进程已结束，退出代码为 0
"""
