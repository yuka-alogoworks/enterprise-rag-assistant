from fastapi import APIRouter

from app.schemas import ChatRequest, ChatResponse, IngestResponse
from app.services.answer_service import answer_question
from app.services.ingest_service import ingest_directory

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/ingest", response_model=IngestResponse)
def ingest():
    indexed_files, indexed_chunks = ingest_directory("data/source_docs")
    return IngestResponse(indexed_files=indexed_files, indexed_chunks=indexed_chunks)


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    result = answer_question(question=request.question, session_id=request.session_id)
    return ChatResponse(**result)
