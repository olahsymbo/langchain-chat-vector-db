[![langchain-chat-vector-db](https://github.com/olahsymbo/langchain-chat-vector-db/actions/workflows/langchain-vector-ci.yaml/badge.svg)](https://github.com/olahsymbo/langchain-chat-vector-db/actions/workflows/langchain-vector-ci.yaml)

# Langchain-Chat-Vector-DB

This is a project that enables users to interact with their documents (PDF, DOCX, or plain text files) using natural language. This chatbot leverages Langchain, Python, ChatGPT, ChromaDB, and OpenAI technologies to provide a seamless conversational experience.

## Features

- Support for PDF, DOCX, and plain text files.
- Natural language processing for document interaction.
- Easy integration with Python 3.8.
- Utilizes ChatGPT for generating conversational responses.
- Efficient document indexing and retrieval using ChromaDB.

## Installation

1. Clone the project repository:

```
git clone https://github.com/olahsymbo/langchain-chat-vector-db.git
```

2. Change into the project directory:

```
cd langchain-chat-vector-db
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Run the application:

```
python app.py
```


## Configuration

The chatbot's behavior can be configured by creating a `.env` file. Here are some key configuration options:

**OPENAI_API_KEY:** Your OpenAI API key. Get it from the OpenAI developer dashboard (https://platform.openai.com).
