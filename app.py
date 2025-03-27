import requests
import os
from dotenv import load_dotenv
import json
import streamlit as st

load_dotenv()
APPLICATION_TOKEN = os.getenv("APP_TOKEN")
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "8eb85d7d-c528-4be6-88c5-4ebec5b46db0"
FLOW_ID = "1bb0d28e-080d-4359-bdcb-b09b88eb0a3e"
ENDPOINT = "customer" # The endpoint name of the flow


def run_flow(message: str) -> dict:
    """
    Run a flow with a given message and optional tweaks.

    :param message: The message to send to the flow
    :param endpoint: The ID or the endpoint name of the flow
    :param tweaks: Optional tweaks to customize the flow
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = None
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    st.title("Astronomy Questions")
    message= st.text_area("Message", placeholder="Enter your question here....")

    if st.button("Submit"):
        if not message.strip():
            st.error("Please enter a message")
            return
        try:
            with st.spinner("Thinking..."):
                result= run_flow(message)
            
            response=result["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()

