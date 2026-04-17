from typing import TypedDict


class ChatState(TypedDict, total=False):
    question: str
    session_id: str
    retrieved_docs: list[dict]
    answer: str
    citations: list[dict]
    used_context: bool
