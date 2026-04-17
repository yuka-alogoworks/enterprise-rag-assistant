from __future__ import annotations

from app.config import settings
from app.llm.ollama_client import embed_texts
from app.retrieval.chroma_store import get_collection


def retrieve_documents(question: str) -> list[dict]:
    collection = get_collection()
    total = collection.count()
    if total == 0:
        return []

    query_embedding = embed_texts([question])[0]
    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(settings.top_k, total),
        include=["documents", "metadatas", "distances"],
    )

    documents = result.get("documents", [[]])[0]
    metadatas = result.get("metadatas", [[]])[0]
    distances = result.get("distances", [[]])[0]

    docs = []
    for doc, metadata, distance in zip(documents, metadatas, distances, strict=False):
        if distance is not None and distance > settings.min_distance:
            continue
        docs.append(
            {
                "text": doc,
                "metadata": metadata or {},
                "distance": distance,
            }
        )
    return docs
