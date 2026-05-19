# RAG — Retrieval-Augmented Generation

A project implementing a Retrieval-Augmented Generation (RAG) pipeline that combines document retrieval with a large language model (LLM) to generate accurate, context-aware responses.

## What is RAG?

RAG is an AI technique that improves LLM responses by first retrieving relevant documents from a knowledge base, then passing them as context to the model before generating an answer. This reduces hallucinations and keeps responses grounded in real data.

## Project Structure

```
RAG/
├── __init__.py          # Package initializer
├── config/
│   └── LLM.yaml         # LLM configuration (model name, temperature, API keys, etc.)
└── README.md            # Project documentation
```

## How It Works

1. **Indexing** — Documents are split into chunks and stored in a vector database
2. **Retrieval** — User query is embedded and matched against stored chunks
3. **Augmentation** — Retrieved chunks are added to the prompt as context
4. **Generation** — LLM generates a response using the retrieved context

## Configuration

Edit `config/LLM.yaml` to set your LLM provider, model, and parameters:

```yaml
model: gpt-4        # or claude-sonnet, mistral, etc.
temperature: 0.7
max_tokens: 1024
```

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python -m RAG
```
