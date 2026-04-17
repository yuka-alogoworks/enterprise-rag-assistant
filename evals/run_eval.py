import json
from pathlib import Path

from app.services.answer_service import answer_question


def main():
    path = Path("evals/goldens.jsonl")
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

    results = []
    for row in rows:
        res = answer_question(row["question"], session_id="eval")
        answer = res["answer"]
        citations = res["citations"]

        answer_non_empty = bool(answer.strip())
        citation_present = bool(citations)
        must_contain_ok = row["must_contain"] in answer
        source_ok = True
        if row["expected_source"]:
            source_ok = any(c["source"] == row["expected_source"] for c in citations)

        results.append(
            {
                "question": row["question"],
                "answer_non_empty": answer_non_empty,
                "citation_present": citation_present,
                "must_contain_ok": must_contain_ok,
                "source_ok": source_ok,
            }
        )

    passed = sum(
        1 for r in results
        if r["answer_non_empty"] and r["must_contain_ok"] and r["source_ok"]
    )
    print(json.dumps({"total": len(results), "passed": passed, "results": results}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
