import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="Robby | Chat-Bot 🤖")


#Contact
with st.sidebar.expander("📬 Contact"):

    st.write("**GitHub:**",
"[AhmedEwis/AI_Assistant](https://github.com/AhmedEwis/AI_Assistant)")


    st.write("**Twitter:** [@sor3a95](https://twitter.com/sor3a95)")
    st.write("**Mail** : ahmed.ewis.ml@gmail.com")
    st.write("**Created by Ahmed Ewis**")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>AI_Assistant, your data-aware assistant 🤖</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>I'm AI_Assistant, an intelligent chatbot created by combining 
    the strengths of Langchain and Streamlit. I use large language models to provide
    context-sensitive natural language interactions. My goal is to help you better understand your data.
    I support PDF, TXT, CSV, Youtube transcript with more coming soon! 🧠</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#Robby's Pages
st.subheader("🚀 AI_Assistant's Pages")
st.write("""
- **AI_Assistant-Chat**: General Chat on data (PDF, TXT,CSV) with a [vectorstore](https://github.com/facebookresearch/faiss) (can't process the whole file just index useful parts(max 4) for respond to the user ) | works with [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html) + (soon) Summarize data
- **AI_Assistant-Sheet** (beta): Chat on tabular data (CSV) | for precise information | can process the whole file (with python code) | works with [CSV_Agent](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html) + [PandasAI](https://github.com/gventuri/pandas-ai) for data manipulation and graph creation (experimental)
- **AI_Assistant-Youtube**: Summarize YouTube videos with [summarize-chain](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html)
- (soon) **AI_Assistant-Lyrics**: Chat and analyze music lyrics | works by scraping lyrics from Genius
- (soon) **AI_Assistant-Github**: Chat over GitHub repositories for understanding the code
- (soon) **AI_Assistant-Website**: Chat with any website you provide
""")
st.markdown("---")


#Contributing
st.markdown("### 🎯 Contributing")
st.markdown("""
**AI_Assistant is under regular development. Feel free to contribute and help me make it even more data-aware!**
""", unsafe_allow_html=True)





