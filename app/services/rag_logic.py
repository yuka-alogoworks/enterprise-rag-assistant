from __future__ import annotations

from app.llm.ollama_client import chat

SYSTEM_PROMPT = """    あなたは社内ドキュメント検索アシスタントです。
必ず日本語で回答してください。
与えられたコンテキストに根拠がある内容だけを回答してください。
根拠が足りない場合は、分からないと明示してください。
"""


def answer_with_context(question: str, docs: list[dict]) -> tuple[str, list[dict]]:
    context_parts = []
    citations: list[dict] = []

    for i, doc in enumerate(docs, start=1):
        metadata = doc.get("metadata", {})
        source = metadata.get("source", "unknown")
        title = metadata.get("title", source)
        snippet = doc["text"][:200]
        context_parts.append(f"[{i}] source={source}\n{doc['text']}")
        citations.append(
            {
                "doc_id": metadata.get("doc_id", f"{source}#chunk-{i}"),
                "title": title,
                "source": source,
                "snippet": snippet,
                "score": doc.get("distance"),
            }
        )

    context = "\n\n".join(context_parts)
    user_prompt = f"""    質問:
{question}

コンテキスト:
{context}

指示:
- コンテキストにある情報だけで答えてください
- 根拠がある場合は文末で [1] [2] のように参照してください
- 根拠が足りない場合は「ドキュメント内に根拠が見つかりませんでした」と回答してください
"""
    answer = chat(SYSTEM_PROMPT, user_prompt)
    return answer, citations


def answer_without_context(question: str) -> str:
    _ = question
    return "ドキュメント内に根拠が見つかりませんでした。担当者または元資料を確認してください。"
