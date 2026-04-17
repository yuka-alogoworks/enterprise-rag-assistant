from typing import List, Optional

from pydantic import BaseModel, Field


class Citation(BaseModel):
    doc_id: str
    title: str
    source: str
    snippet: str
    score: Optional[float] = None


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1)
    session_id: str = Field(default="anonymous")


class ChatResponse(BaseModel):
    answer: str
    citations: List[Citation] = []
    used_context: bool = False


class IngestResponse(BaseModel):
    indexed_files: int
    indexed_chunks: int
