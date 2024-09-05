import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv

load_dotenv()

# # Environment Setup
# st.secrets["LANGCHAIN_TRACING_V2"] = "true"
# st.secrets['LANGCHAIN_API_KEY'] = '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'
# st.secrets['LANGCHAIN_PROJECT'] = 'Langchain - Chat with Search'

# Arxiv and Wikipedia Wrappers
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=1000)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

wikipedia_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=1000)
wikipedia = WikipediaQueryRun(api_wrapper=wikipedia_wrapper)

# DuckDuckGo Search Tool
search = DuckDuckGoSearchRun(name="Search")

# Streamlit Title
st.title("Langchain - Chat with Search")
"""
In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
Try more LangChain 🤝 Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
"""

# Sidebar for Settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant",
         "content": "Hi, I am a Chatbot who can search the Web. How can I help you?"}
    ]

# Display conversation history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat input
if prompt := st.chat_input(placeholder="What is Machine Learning?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # LLM Model
    llm = ChatGroq(groq_api_key=api_key, model_name='llama3-8b-8192', streaming=True)

    # Tools
    tools = [search, arxiv, wikipedia]

    # Agent with Parsing Error Handling
    search_agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True  
    )

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        try:
            response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
            st.session_state.messages.append({'role': 'assistant', 'content': response})
            st.write(response)
        except Exception as e:
            st.write(f"An error occurred: {e}")
