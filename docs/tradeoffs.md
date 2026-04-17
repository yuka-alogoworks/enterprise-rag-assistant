# Trade-offs

## Why Chroma
ローカル永続化が簡単で、PoC を早く作れるため。

## Why local Ollama
API コストを抑えながら、面談時に自前 PC で再現しやすいため。

## Why Markdown-first
文書ローダーの複雑性を減らし、最初の品質検証に集中するため。

## What to improve for production
- 認証
- 監査ログ
- 可観測性
- 非同期 ingest
- アップロード UI
