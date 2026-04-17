from langgraph.graph import END, START, StateGraph

from app.graph.state import ChatState
from app.retrieval.retriever import retrieve_documents
from app.services.rag_logic import answer_with_context, answer_without_context


def _retrieve(state: ChatState) -> ChatState:
    docs = retrieve_documents(state["question"])
    return {"retrieved_docs": docs}


def _route(state: ChatState) -> str:
    if state.get("retrieved_docs"):
        return "with_context"
    return "without_context"


def _answer_with_context(state: ChatState) -> ChatState:
    answer, citations = answer_with_context(state["question"], state["retrieved_docs"])
    return {"answer": answer, "citations": citations, "used_context": True}


def _answer_without_context(state: ChatState) -> ChatState:
    answer = answer_without_context(state["question"])
    return {"answer": answer, "citations": [], "used_context": False}


def build_chat_graph():
    graph = StateGraph(ChatState)
    graph.add_node("retrieve", _retrieve)
    graph.add_node("with_context", _answer_with_context)
    graph.add_node("without_context", _answer_without_context)

    graph.add_edge(START, "retrieve")
    graph.add_conditional_edges(
        "retrieve",
        _route,
        {
            "with_context": "with_context",
            "without_context": "without_context",
        },
    )
    graph.add_edge("with_context", END)
    graph.add_edge("without_context", END)
    return graph.compile()
