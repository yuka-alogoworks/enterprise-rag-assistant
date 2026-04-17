from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ollama_base_url: str = "http://localhost:11434/api"
    ollama_chat_model: str = "gemma3"
    ollama_embed_model: str = "embeddinggemma"
    chroma_dir: str = "./data/chroma"
    chroma_collection: str = "documents"
    top_k: int = 5
    min_distance: float = 1.2
    max_chunk_size: int = 800
    chunk_overlap: int = 120
    allow_empty_context: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
