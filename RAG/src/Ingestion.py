from datasets import load_from_disk
import ast
from langchain_text_splitters import RecursiveCharacterTextSplitter

DATASET_PATH = '/Users/ghulammustafa/Desktop/Projects/Foundation/MLFoundations/RAG/rag-instruct/train'


def load_chunks():
    ds = load_from_disk(DATASET_PATH)
    df = ds.to_pandas()

    all_docs = []
    for _, row in df.iterrows():
        docs = row['documents']
        if isinstance(docs, str):
            docs = ast.literal_eval(docs)
        for doc in docs:
            all_docs.append({
                "text": doc,
                "question": row['question'],
                "answer": row['answer']
            })

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=64,
        separators=["\n\n", "\n", ". ", " ", ""]
    )

    chunked_docs = []
    for doc in all_docs:
        chunks = splitter.split_text(doc["text"])
        for i, chunk in enumerate(chunks):
            chunked_docs.append({
                "chunk_text": chunk,
                "chunk_id": i,
                "source_question": doc["question"],
                "source_answer": doc["answer"]
            })

    return chunked_docs


if __name__ == "__main__":
    chunks = load_chunks()
    print(f"Total chunks: {len(chunks)}")
