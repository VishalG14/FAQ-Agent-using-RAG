#General FAQ Agent with RAG
Project Overview
Welcome to the General FAQ Agent! This project leverages Retrieval-Augmented Generation (RAG) to create a versatile FAQ agent for answering customer queries based on any company-provided PDF. Built using Langflow, it consists of two flows: one to ingest a PDF into an Astra DB vector database, and another to answer questions by querying the vector database with stored PDF data.

Features
Upload any company PDF to power the FAQ agent.
Answers queries using RAG by looking up the vector database.
Configurable with your preferred LLM and API keys.
Adaptable for any domain based on the input PDF.
Prerequisites
Langflow: Install Langflow to run the flows (follow Langflow's official setup guide).
Astra DB Account: Set up an Astra DB account for the vector database (sign up at Astra DB).
LLM API Key: Obtain an API key for your chosen LLM provider (e.g., Google Generative AI, OpenAI, etc.).
A PDF file with the data you want the FAQ agent to use.
Setup Instructions
Clone the Repository
bash

Collapse

Wrap

Copy
git clone https://github.com/your-username/general-faq-agent.git
cd general-faq-agent
Install Langflow
Follow the Langflow installation guide to set up the environment:
Install via pip: pip install langflow
Start Langflow: langflow run
Configure Astra DB
Create a vector database in Astra DB.
Note your Astra DB API endpoint, token, and database ID for use in the flows.
Import the Flows
In Langflow, import the two flows from the flows/ directory in this repo:
ingest_pdf_to_astra.json: Ingests your PDF into the Astra DB vector database.
query_vector_db.json: Queries the vector database to answer user questions.
To import, click "Import" in Langflow and select the respective .json file.
Configure the Agent
Open the query_vector_db flow in Langflow.
Set your LLM provider (e.g., Google Generative AI, OpenAI) and input your API key.
Configure the Astra DB connection with your endpoint, token, and database ID.
(Optional) Adjust "Max Output Tokens" (e.g., 500 tokens) for optimal response length.
Run the Ingest Flow
Run the ingest_pdf_to_astra flow.
Upload your PDF when prompted. This will process the PDF and store its data in the Astra DB vector database.
Run the Query Flow
Run the query_vector_db flow.
Input a customer question, and the agent will retrieve relevant info from the vector database to answer.
Usage
Integrate the query flow into your application to provide automated FAQ responses.
Update the PDF in the ingest flow to adapt the agent for different datasets.
Contributing
Feel free to fork this repo, submit issues, or contribute improvements via pull requests!

License
This project is licensed under the MIT License. See the LICENSE file for details.
