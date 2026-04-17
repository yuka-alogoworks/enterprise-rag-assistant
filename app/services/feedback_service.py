from __future__ import annotations

import json
from pathlib import Path


def save_feedback(payload: dict, path: str = "data/feedback.jsonl") -> None:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")
