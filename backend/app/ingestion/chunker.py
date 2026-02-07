def make_chunks(entries):
    chunks = []
    for e in entries:
        text = f"{e['prompt']} {e['completion']}"
        chunks.append({
            "text": text,
            "metadata": e.get("metadata", {})
        })
    return chunks


# Chunk = piece of text stored in vector DB