from app.graph.workflow import build_chat_graph


def answer_question(question: str, session_id: str) -> dict:
    graph = build_chat_graph()
    state = graph.invoke({"question": question, "session_id": session_id})
    return {
        "answer": state["answer"],
        "citations": state.get("citations", []),
        "used_context": state.get("used_context", False),
    }
