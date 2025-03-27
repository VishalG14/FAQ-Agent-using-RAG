
# General FAQ Agent with RAG 🌟
### Project Overview 📖

Welcome to the General FAQ Agent! 🎉 This project leverages Retrieval-Augmented Generation (RAG) to create a versatile FAQ agent for answering customer queries based on any company-provided PDF. 📄 Built using Langflow 🚀, it consists of two flows: one to ingest a PDF into an Astra DB vector database, and another to answer questions by querying the vector database with stored PDF data. 🔍

### Features ✨

- Upload any company PDF to power the FAQ agent. 📤
- Answers queries using RAG by looking up the vector database. 🗄️
- Configurable with your preferred LLM and API keys. 🔧
- Adaptable for any domain based on the input PDF. 🌍

### Prerequisites ✅
- Langflow: Install Langflow to run the flows (follow [Langflow's official setup guide](https://docs.langflow.org)). 🛠️
- Astra DB Account: Set up an Astra DB account for the vector database (sign up at [Astra DB](https://www.datastax.com/products/datastax-astra)). ☁️
- LLM API Key: Obtain an API key for your chosen LLM provider (e.g., Google Generative AI, OpenAI, etc.). 🔑
- A PDF file with the data you want the FAQ agent to use. 📜

### Setup Instructions 🛠️
1. Clone the Repository 📂
```bash
git clone https://github.com/VishalG14/FAQ-Agent-using-RAG.git
cd FAQ-Agent-using-RAG
```
2. Install Langflow 💻
```python
pip install langflow
langflow run
```
Or just use it online.

3. Configure Astra DB ☁️
- Create a vector database in Astra DB.
- Note your Astra DB API endpoint, token, and database ID for use in the flows. 📝
4. Import the Flows 📥
- To import, click "Import" in Langflow and select the respective flow.json file.
5. Configure the Agent ⚙️
- Set your LLM provider (e.g., Google Generative AI, OpenAI) and input your API key. 🔑
- Configure the Astra DB connection with your endpoint, token, and database ID. 🔗
- (Optional) Adjust "Max Output Tokens" (e.g., 500 tokens) for optimal response length. 📏
6. Run the Ingest Flow 🚀
- In langflow, upload your PDF in file injestion agent. This will process the PDF and store its data in the Astra DB vector database. 📦
7. Run the Query Flow ❓

- Input a customer question, and the agent will retrieve relevant info from the vector database to answer. 💬

### Usage 🌐
Integrate the query flow into your application to provide automated FAQ responses. 🤖
Update the PDF in the ingest flow to adapt the agent for different datasets. 🔄

### License 📜
This project is licensed under the MIT License. See the  file for details.
