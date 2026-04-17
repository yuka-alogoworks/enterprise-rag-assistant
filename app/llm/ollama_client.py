from __future__ import annotations

import httpx

from app.config import settings


def embed_texts(texts: list[str]) -> list[list[float]]:
    response = httpx.post(
        f"{settings.ollama_base_url}/embed",
        json={"model": settings.ollama_embed_model, "input": texts},
        timeout=60.0,
    )
    response.raise_for_status()
    return response.json()["embeddings"]


def chat(system_prompt: str, user_prompt: str) -> str:
    response = httpx.post(
        f"{settings.ollama_base_url}/chat",
        json={
            "model": settings.ollama_chat_model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "stream": False,
        },
        timeout=120.0,
    )
    response.raise_for_status()
    data = response.json()
    return data["message"]["content"].strip()
