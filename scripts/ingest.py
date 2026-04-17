from app.services.ingest_service import ingest_directory


def main() -> None:
    indexed_files, indexed_chunks = ingest_directory("data/source_docs")
    print({"indexed_files": indexed_files, "indexed_chunks": indexed_chunks})


if __name__ == "__main__":
    main()
