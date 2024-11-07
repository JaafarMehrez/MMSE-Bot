# MMSE-Bot

MMSE-Bot is a [Chatbot](https://en.wikipedia.org/wiki/Chatbot) based on questions and accepted/top-voted answers from [MMSE](https://mattermodeling.stackexchange.com)

Data is obtained with Python Stackexchange API Wrapper library [StackAPI](https://stackapi.readthedocs.io/)

The chatbot is built with local LLM and embedding models. In specific, [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5) as embedding model and [Llama3](https://www.llama.com/docs/overview) through [Ollama](https://ollama.com).

Your directory structure should look like this:

    ├── Starter.py
    └── data
       └── Q&A.txt
    ├── src
       └── FetchData.py

The src/ folder contains the API wrapper and the method for fetching and parsing the data. Starter.py builds an index over the documents in the data/ folder (which in this case consists of the questions and answers fetched from MMSE). The Starter.py would also create an engine for Q&A over your index and respond to your queries.
