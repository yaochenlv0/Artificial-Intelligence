import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 读取text文件
def read_txt_file(file_path):
    # 正常运行
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            text = file.read()
        return text
    # 如果出错，并且属于FileNotFoundError，则
    except FileNotFoundError:
        print(f"错误：文件{file_path}未找到")
        return None
    # 如果出错，并且是其他错误，则
    except Exception as e:
        print(f"读取文件时出错：{e}")
        return None

# 调用模型生成文本摘要
def generate_summary(text,max_tokens=500):
    try:
        response = client.chat.Completion.create(
            model = 'deepseek-chat',
            # Prompt 是输入给大模型的上下文信息，包括角色设定（system）、任务指令（user）以及相关数据（如文本内容）。模型根据这些信息生成符合要求的输出结果。
            messages=[
                {"role":"system","content":"你是一个专业的文本总结助手。请用简洁、准确的语言总结用户提供的文本内容，抓住要点。"},
                {"role":"user","content":f"请总结一下文本：{text}"}
            ],
            # 最多生成500token的内容，大概1token=0.75单词、1个汉字=1-2个token、一个标点=1个token
            # 500token=300-400个文字内容
            max_tokens=max_tokens,
            # 降低随即性使输出更稳定
            temperature=0.3
        )
        summary = response.choices[0].message.content
        return summary
    except Exception as e:
        print(f"调用模型时出错：{e}")

def main():
    # 指定要读的txt文件路径
    file_path="input.txt"

    # 读取文件
    print(f"正在读取文件：{file_path}")
    text = read_txt_file(file_path)

    if text is None:
        # return None 等价 return 等价 pass(函数结束自动返回None)
        return

    print(f"成功读取文本，长度：{len(text)}字符")
    print("\n"+"="*50)
    print("原始文本预览（前500字符）：")
    print("="*50+"\n")

    # 生成摘要
    print("正在生成摘要...")
    summary = generate_summary(text)

    if summary is None:
        return

    print("\n"+"="*50)
    print("文本摘要：")
    print(summary)
    print("="*50)

    # 可选 将摘要部分保存到文件
    with open("summary.txt","w",encoding="utf-8") as f:
        f.write(summary)
    print("摘要已保存到 summary.txt")

if __name__=="__main__":
    main()

