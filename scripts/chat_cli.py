from app.services.answer_service import answer_question


def main():
    while True:
        question = input("question> ").strip()
        if not question:
            continue
        if question.lower() in {"exit", "quit"}:
            break
        result = answer_question(question, session_id="cli")
        print("\nanswer:", result["answer"])
        print("citations:")
        for citation in result["citations"]:
            print(f" - {citation['source']}: {citation['snippet'][:100]}")
        print()


if __name__ == "__main__":
    main()
