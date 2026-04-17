from app.services.ingest_service import ingest_directory


if __name__ == "__main__":
    indexed_files, indexed_chunks = ingest_directory("data/source_docs")
    print({"indexed_files": indexed_files, "indexed_chunks": indexed_chunks})
