import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# 从环境变量中读取 API Key
api_key = os.getenv("ARK_API_KEY")
# 设置火山的Base URL
base_url = "https://ark.cn-beijing.volces.com/api/v3"
# 设置模型
MODEL = "doubao-seed-1-8-251228"

# 初始化客户端
client = OpenAI(api_key=api_key, base_url=base_url)

def translate_text(text, target_language="英文"):
    """翻译文本到目标语言"""
    prompt = f"""你是一位专业的翻译专家。请将以下文本翻译成{target_language}。
只返回翻译结果，不要添加任何额外说明。

文本：{text}"""
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

def summarize_text(text, max_length=200):
    """生成文本摘要"""
    prompt = f"""你是一位资深的文案编辑。请为以下文本生成一段简洁的摘要。
要求：摘要长度控制在{max_length}字以内，抓住核心要点，语言精练。

文本：{text}"""
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content

def translate_and_summarize(text, target_language="英文"):
    """先翻译再摘要"""
    translated = translate_text(text, target_language)
    summary = summarize_text(translated)
    return {"translation": translated, "summary": summary}

