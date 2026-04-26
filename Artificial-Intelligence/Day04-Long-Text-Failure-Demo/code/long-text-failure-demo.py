import os
from openai import OpenAI

# 创建客户端
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 读取长文本文件
def read_txt_file(file_path):
    try:
        with open(file_path,'r',encoding="uft-8") as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"错误：文件{file_path}不存在")
        return None
    except Exception as e:
        print(f"读取文件失败：{e}")
        return None

# 直接将长文本喂给大模型总结
def summarize_long_text_directly(text):
    try:
        responses = client.chat.Completion.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": "你是一个文本总结助手，请对用户提供的长文本进行总结。"
                 },
                {
                    "role": "user",
                    "content": f"请总结下面这篇文本：{text}"
                }
            ],
            # 不采用流式传输
            stream=False
        )
        return responses.choices[0].message.content
    except Exception as e:
        print(f"调用模型失败：{e}")
        return None

if __name__=="__main__":
    file_path="long_text.txt"

    text = read_txt_file(file_path)

    if text is not None:
        print("文本读取成功")
        print(f"文本长度：{len(text)}个字符")
        summary = summarize_long_text_directly(text)
        if summary:
            print("=====模型总结结果=====")
            print(summary)
            with open("失败案例记录.md","w",encoding="utf-8") as file:
                file.write("Day04-Long-Text-Failure-Demo-Summary")
                file.write("一、实验方式\n\n")
                file.write("本次文件将一片较长文本完整输入给大模型，让模型进行总结。\n\n")
                file.write("二、原始文件长度\n\n")
                file.write(f"原始文件长度约为：{len(text)}个字符。\n\n")
                file.write("三、模型总结结果\n\n")
                file.write(summary)
                file.write("\n\n")
                file.write("四、可能发现的问题\n\n")
                file.write("1.总结可能遗漏了部分重要内容\n")
                file.write("2.对长文本中的细节信息概括的不完整\n")
                file.write("3.总结内容泛泛而谈，不能概括全文结构\n")
                file.write("4.如果文本内容继续变长，可能会超出模型上下文限制\n\n")
                file.write("五、我的理解\n\n")
                file.write("长文本不能简单直接全部喂给大模型处理，需要先进行文本切分，再分段总结，最后汇总结果\n")
            print("\n失败案例记录.md 已生成")
