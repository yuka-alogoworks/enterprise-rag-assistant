from app.services.rag_logic import SYSTEM_PROMPT


def test_system_prompt_contains_guardrail():
    assert "日本語" in SYSTEM_PROMPT
    assert "根拠" in SYSTEM_PROMPT
