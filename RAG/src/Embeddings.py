import torch
from tqdm import tqdm
from langchain_huggingface import HuggingFaceEmbeddings
from Ingestion import load_chunks
import numpy as np
# Prefer MPS (Apple Silicon) > CUDA > CPU
if torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"

print(f"Using device: {device}")

model_name = "sentence-transformers/all-MiniLM-L6-v2"
model_kwargs = {'device': device}
encode_kwargs = {'normalize_embeddings': False}

hf = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

chunked_docs = load_chunks()
texts = [doc["chunk_text"] for doc in chunked_docs]

embeddings = []
for text in tqdm(texts, desc="Embedding chunks"):
    embeddings.append(hf.embed_query(text))

print(f"Total chunks embedded: {len(embeddings)}")
print(f"Embedding dimension:   {len(embeddings[0])}")



np.save("embeddings.npy", np.array(embeddings))
print("Embeddings saved to embeddings.npy")