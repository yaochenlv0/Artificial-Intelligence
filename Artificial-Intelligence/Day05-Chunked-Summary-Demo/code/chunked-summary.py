import os
from openai import OpenAI

# 创建客户端
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek,com"
)

# 读取文本文件
def read_text_file(file_path):
    try:
        with open(file_path,'r',encoding="utf-8") as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"错误：文件{file_path}不存在")
        return None
    except Exception as f:
        print(f"读取文件失败：{e}")
        return None

# 将长文本切分为多个chunk
# chunk_size=1000 每一个chunk最多包含1000个字符
def split_text(text,chunk_size=1000):
    chunks = []

    for i in range(0,len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        chunks.append(chunk)
    return chunks

# 总结单个chunk文本
def summarize_chunk(chunk):
    try:
        responses = client.chat.completion.create(
            model = "deepseek-chat",
            messages = [
                {"role": "system", "content": "你是一个专业的文本总结助手，请用简洁清晰的语言总结用户提供的文本。"},
                {"role": "user", "content": f"请总结下面这段文本：\n{chunk}"}
            ],
            stream = False
        )
        summary = responses.choices[0].message.content
        return summary
    except Exception as e:
        print(f"总结chunk失败：{e}")
        return None

# 对所有chunk分别总结
def summarize_chunks(chunks):
    chunk_summaries = []
    for index,chunk in enumerate(chunks):
        print(f"正在总结第{index+1}个chunk...")

        summary = summarize_chunk(chunk)

        if summary:
            chunk_summaries.append(summary)

    return chunk_summaries

# 汇总所有分段摘要
def summarize_final(chunk_summaries):
    try:
        summarizes_text = "\n\n".join(chunk_summaries)

        response = client.chat.completions.create(
            model = "deepseek-chat",
            messages = [
                {"role": "system", "content": "你是一个专业的总结助手，请将多个分段摘要整合成一个完整、清晰、有重点的总摘要。"},
                {"role": "user", "content": f"请根据下面的分段摘要，生成一份总摘要：{summarizes_text}"}
            ],
            stream = False
        )

        final_summary = response.choices[0].message.content
        return final_summary
    except Exception as e:
        print(f"生成摘要失败：{e}")
        return None

# 主函数
def main():
    file_path = "文本.txt"
    text = read_text_file(file_path)
    if text is None:
        return

    chunks = split_text(text, chunk_size=1000)
    print(f"文本切分完成，共切分为{len(chunks)}个chunk")
    chunk_summaries = summarize_chunks(chunks)
    final_summary= summarize_final(chunk_summaries)
    if final_summary:
        print("=====最终总摘要=====")
        print(final_summary)

if __name__=="__main__":
    main()