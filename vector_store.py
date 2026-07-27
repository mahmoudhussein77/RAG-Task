import faiss
import numpy as np
from pdf_processing import chunks
from sources import saving_faiss_index_path
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):

    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(texts, convert_to_numpy=True)

    return embeddings


embedding = create_embeddings(chunks)



def create_faiss_index(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings.astype(np.float32))

    return index


faiss_index = create_faiss_index(embedding)


faiss.write_index(faiss_index, saving_faiss_index_path)


def search(query, k=3):

    query_vector = model.encode([query], convert_to_numpy=True).astype(np.float32)

    distances, indices = faiss_index.search(query_vector, k)

    results = []

    for i, idx in enumerate(indices[0]):

        if idx == -1:
            continue

        results.append(
            {
                "page": chunks[idx]["page"],
                "text": chunks[idx]["text"],
                "distance": float(distances[0][i])
            }
        )

    return results