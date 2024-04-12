"""
This is the web frontend of PoisonGPT.

It is built using Streamlit.
"""

import streamlit as st


def main():

    st.set_page_config(
        page_title = "PoisonGPT",
        page_icon = "🤖"
    )

    st.header("PoisonGPT 🤖")

    st.markdown("PoisonGPT is developped to illustrate **poisoning attacks** against LLM RAG applications. " \
                "This chatbot is a cybersecurity expert and can give great cybersecurity advice thanks " \
                "to its database of recommandations and best practices. _For now ..._")

    # container for user questions and responses
    chat_container = st.container()

    chat_container.markdown("## Ask your questions")

    st.chat_input("Enter your question ...")

if __name__ == '__main__':
    main()