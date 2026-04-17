from app.retrieval.chunking import chunk_text


def test_chunk_text_splits_large_input():
    text = "a" * 2000
    chunks = chunk_text(text)
    assert len(chunks) >= 2
    assert all(isinstance(chunk, str) for chunk in chunks)
