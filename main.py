from langchain_experimental.agents import create_csv_agent
from langchain_community.llms import OpenAI
import os
import streamlit as st


def main():

    os.environ["OPENAI_API_KEY"] = "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"


   

    st.set_page_config(page_title="Ask CSV")
    st.header("Ask anythink you want : 🚀")

    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    pdf_file = st.file_uploader("Upload a PDF file (not implemented yet)", type="pdf")
    txt_file = st.file_uploader("Upload a CSV file (not implemented yet)", type="txt")
    
    if csv_file is not None:

        agent = create_csv_agent(
            OpenAI(temperature=0), csv_file, verbose=True)

        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))


if __name__ == "__main__":
    main()
