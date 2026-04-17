from __future__ import annotations

from pathlib import Path

from app.llm.ollama_client import embed_texts
from app.retrieval.chroma_store import get_collection
from app.retrieval.chunking import chunk_text


def ingest_directory(directory: str) -> tuple[int, int]:
    collection = get_collection()
    root = Path(directory)
    indexed_files = 0
    indexed_chunks = 0

    for path in sorted(root.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        chunks = chunk_text(text)
        if not chunks:
            continue

        embeddings = embed_texts(chunks)
        ids = [f"{path.name}#chunk-{i}" for i in range(len(chunks))]
        metadatas = [
            {
                "doc_id": ids[i],
                "source": path.name,
                "title": path.stem,
            }
            for i in range(len(chunks))
        ]

        collection.upsert(
            ids=ids,
            documents=chunks,
            metadatas=metadatas,
            embeddings=embeddings,
        )
        indexed_files += 1
        indexed_chunks += len(chunks)

    return indexed_files, indexed_chunks
