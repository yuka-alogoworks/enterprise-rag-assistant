from pydantic import BaseModel, Field


class Citation(BaseModel):
    doc_id: str
    title: str
    source: str
    snippet: str
    score: float | None = None


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1)
    session_id: str = Field(default="anonymous")


class ChatResponse(BaseModel):
    answer: str
    citations: list[Citation] = Field(default_factory=list)
    used_context: bool = False


class IngestResponse(BaseModel):
    indexed_files: int
    indexed_chunks: int
