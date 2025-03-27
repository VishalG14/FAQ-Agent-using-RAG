
# General FAQ Agent with RAG 🌟
### Project Overview 📖

Welcome to the General FAQ Agent! 🎉 This project leverages Retrieval-Augmented Generation (RAG) to create a versatile FAQ agent for answering customer queries based on any company-provided PDF. 📄 Built using Langflow 🚀, it consists of two flows: one to ingest a PDF into an Astra DB vector database, and another to answer questions by querying the vector database with stored PDF data. 🔍

### Features ✨

1. Upload any company PDF to power the FAQ agent. 📤
2. Answers queries using RAG by looking up the vector database. 🗄️
3. Configurable with your preferred LLM and API keys. 🔧
4. Adaptable for any domain based on the input PDF. 🌍

### Prerequisites ✅
1. Langflow: Install Langflow to run the flows (follow [Langflow's official setup guide]{https://docs.langflow.org}). 🛠️
2. Astra DB Account: Set up an Astra DB account for the vector database (sign up at Astra DB). ☁️
3. LLM API Key: Obtain an API key for your chosen LLM provider (e.g., Google Generative AI, OpenAI, etc.). 🔑
4. A PDF file with the data you want the FAQ agent to use. 📜
