import streamlit as st
from ai_services import translate_text,summarize_text, translate_and_summarize

st.set_page_config(page_title="AI 智能翻译与摘要助手", page_icon="🤖", layout="wide")

st.title("AI 智能翻译与摘要助手")
st.markdown("输入任意文本，AI帮你翻译和提炼精华")

# 侧边栏配置
with st.sidebar:
    st.header("⚙️ 设置")
    operation = st.radio(
        "选择操作",
        ["翻译", "摘要", "翻译 + 摘要"]
    )
    if operation in ["翻译", "翻译 + 摘要"]:
        target_lang = st.selectbox(
            "目标语言",
            ["英文", "中文", "日文", "韩文", "法文", "德文", "西班牙文"]
        )
    if operation == "摘要":
        max_len = st.slider("摘要长度（字数）", 50, 500, 200)

# 主区域
input_text = st.text_area(
    "📝 输入待处理的文本",
    height=200,
    placeholder="请在这里粘贴或输入你要处理的文本..."
)

if st.button("🚀 开始处理", type="primary"):
    if not input_text.strip():
        st.warning("请输入文本")
    else:
        with st.spinner("AI正在处理中..."):
            try:
                if operation == "翻译":
                    result = translate_text(input_text, target_lang)
                    st.subheader("✅ 翻译结果")
                    st.write(result)
                elif operation == "摘要":
                    result = summarize_text(input_text, max_len)
                    st.subheader("✅ 摘要结果")
                    st.write(result)
                else:  # 翻译 + 摘要
                    result = translate_and_summarize(input_text, target_lang)
                    col1, col2 = st.columns(2)
                    with col1:
                        st.subheader("🌐 翻译结果")
                        st.write(result["translation"])
                    with col2:
                        st.subheader("📄 摘要结果")
                        st.write(result["summary"])
            except Exception as e:
                st.error(f"处理失败：{e}")

st.markdown("---")
st.caption("💡 提示：本应用调用大模型API，处理结果仅供参考")