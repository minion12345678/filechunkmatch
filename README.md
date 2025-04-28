🤖 Doc Bot

This project lets you split a text file into chunks and search for the closest matching chunk based on a user's question.

It is a simple and fast way to find relevant parts of large text files without manually reading the entire file.

🚀 Features

Splits a file into manageable text chunks (default: 1024 characters at a time).

Accepts user questions and finds the most relevant chunk based on word overlap.

Handles missing files gracefully (exits with an error if file is not found).

Easy to extend with more advanced matching (e.g., fuzzy matching, semantic search).

📦 Requirements

Python 3.7 or higher

No external libraries needed (only built-in modules: sys)

🛠 How to Use

Prepare a .txt file with the content you want to search.

Open a terminal and run:

python doc_bot.py path/to/your/file.txt
Once running, you can ask questions about the content.

To exit, simply type:
exit

📋 Example

Suppose your file (example.txt) contains:

The quick brown fox jumps over the lazy dog.
Python is a powerful programming language.
Artificial Intelligence is transforming the world.
Databases store and retrieve information efficiently.

You run:
python doc_bot.py example.txt
Then you type:

programming language
Output:

Best matching chunk:

Python is a powerful programming language.
✅ Done!

⚡ How Matching Works

The search is simple keyword matching:

Your question is split into words.

Each chunk is also split into words.

The chunk with the most words in common with your question is selected.

❗ Important Notes

If the file is not found, the program will print an error and exit immediately.

The current matching is case-insensitive but basic (no stemming, no fuzzy matching).

Chunks are split based on character size, not by paragraph or meaning.

🔥 Future Improvements (Optional Ideas)

Add fuzzy matching using difflib for better partial matches.

Implement semantic search with vector embeddings (e.g., using sentence-transformers).

Allow adjustable chunk sizes and smarter splitting (by paragraphs, sections, etc.).

Save the matching results into a file.

👨‍💻 Author
Written by Alexis Newell

