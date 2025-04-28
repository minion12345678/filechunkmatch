import sys

def load_chunks(file_path, chunk_size=1024):
    """Reads a file and splits it into chunks."""
    chunks = []
    try:
        with open(file_path, 'r') as f:
            leftover = ''
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                chunk = leftover + chunk
                lines = chunk.splitlines(keepends=True)

                if not chunk.endswith('\n'):
                    leftover = lines.pop()
                else:
                    leftover = ''

                chunks.extend(lines)
            if leftover:
                chunks.append(leftover)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        sys.exit(1)
    return chunks


def find_best_chunk(chunks, query):
    """Finds the chunk that matches the query best."""
    best_score = -1
    best_chunk = None

    query_words = set(query.lower().split())

    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        score = len(query_words.intersection(chunk_words))  # simple overlap

        if score > best_score:
            best_score = score
            best_chunk = chunk

    return best_chunk


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    chunks = load_chunks(file_path)

    while True:
        query = input("\nAsk a question (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        best_match = find_best_chunk(chunks, query)
        print("\nBest matching chunk:\n")
        print(best_match)
