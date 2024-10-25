## LangChain Chatbot with Search Capabilities
This project is a Streamlit application that leverages LangChain to create an interactive chatbot capable of searching the web for information. The application integrates with various APIs, including Arxiv, Wikipedia, and DuckDuckGo, allowing users to ask questions and receive responses enriched with external data.

## Features
- Conversational Agent: The chatbot can engage users in a conversational manner, providing answers to a variety of queries.
- Web Search Integration: Users can search for information using DuckDuckGo, and retrieve articles from Arxiv and Wikipedia based on their queries.
- Streaming Responses: The chatbot can provide streaming responses, enhancing the user experience by displaying responses as they are generated.
- Session Management: Maintains conversation history using Streamlit session state, allowing users to see previous messages in the chat.

## Technologies Used
- Streamlit: A framework for building interactive web applications.
- LangChain: A framework for building applications with language models, enabling easy integration with various APIs and tools.
- Arxiv API: Used to fetch research papers and articles related to user queries.
- Wikipedia API: Provides quick access to Wikipedia articles.
- DuckDuckGo API: Allows for web searches and retrieving search results.

##Installation
To run this project locally, follow these steps:
- Clone the repository:

  git clone https://github.com/Pranav160702/Search-Engine-With-Langchain-Tools-And-Agents.git

- Install the required dependencies:

  pip install -r requirements.txt
  
- Set up your Groq API key:

  Sign up at Groq and obtain your API key.

- Run the Streamlit app:

  streamlit run app.py

- Open your web browser and go to http://localhost:8501 to interact with the chatbot.

- Usage
  Enter your queries in the chat input field.
  The chatbot will respond using the integrated search tools, fetching relevant information and displaying it in the chat.
  You can continue the conversation, and the chatbot will remember the context.
