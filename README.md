# PoisonGPT

PoisonGPT is a chatbot built to illustrate poisonning attacks on AI applications in the context of RAG (Retrieval Augmented Generation) LLM apps.

This chatbot is built in Python using:
- 🚀 [Streamlit](https://streamlit.io/) - For the web front-end
- 🦙 [Ollama](https://ollama.com/) - To run the models locally
- 🗃️ [Chroma DB](https://www.trychroma.com/) - For the vector database
- 🔗 [LangChain](https://www.langchain.com/) - to link everything together

The models used by the app are:
- [nomic-embed-text](https://blog.nomic.ai/posts/nomic-embed-text-v1) - For the embeddings
- [Mistral-7B](https://mistral.ai/fr/technology/#models) - For the text generation


**Disclaimer:** This app runs both the embedding model and the LLM locally. This process can take a lot of time if you run it without a GPU.




## Installation

To run the app, you will need:
- Ollama, with the appropriate models downloaded
- Python 3, with the required libraries

### Ollama & AI models

First, install Ollama:
- For Windows and MacOS users: download the installation package from https://ollama.com/.
- For Linux users, run the following command:

```
curl -fsSL https://ollama.com/install.sh | sh
```

Then download the models:

```
ollama pull nomic-embed-text
ollama pull mistral
```

To start the Ollama service (if the automatic execution failed):
```
ollama serve
``` 

### Python librairies

To run the app, you need to install the required Python libraries:

```bash
pip install streamlit langchain chromadb
```

## Usage

Once the installation process is complete, run the app using:

```
streamlit run poisongpt.py
```