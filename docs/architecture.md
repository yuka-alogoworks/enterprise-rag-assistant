# Architecture

- API 層: FastAPI
- Workflow 層: LangGraph
- Retrieval 層: Chroma + local embeddings
- Generation 層: Ollama local chat model

## Request Flow
1. `/chat` に質問を送る
2. LangGraph が retrieval ノードを実行
3. 関連ドキュメントがあれば context 付きで回答
4. なければ安全側にフォールバック
5. 根拠候補とともにレスポンスを返す
