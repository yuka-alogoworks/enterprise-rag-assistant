from __future__ import annotations

from app.config import settings


def chunk_text(text: str) -> list[str]:
    text = text.strip()
    if not text:
        return []

    max_size = settings.max_chunk_size
    overlap = settings.chunk_overlap

    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = min(start + max_size, len(text))
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end == len(text):
            break
        start = max(0, end - overlap)
    return chunks
