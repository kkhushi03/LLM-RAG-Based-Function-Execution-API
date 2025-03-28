import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Define function metadata
function_descriptions = {
    "open_chrome": "Launch Google Chrome browser.",
    "open_calculator": "Open the system calculator.",
    "open_notepad": "Launch Notepad application.",
    "get_cpu_usage": "Retrieve current CPU usage percentage.",
    "get_ram_usage": "Retrieve current RAM usage percentage.",
    "run_shell_command": "Execute a shell command in the terminal."
}

# Convert function descriptions to embeddings
db = chromadb.PersistentClient(path="./function_db")
collection = db.get_or_create_collection("function_embeddings")

for function, description in function_descriptions.items():
    embedding = embedding_model.encode(description).tolist()
    collection.add(ids=[function], embeddings=[embedding], metadatas=[{"function": function}])

def retrieve_best_function(prompt):
    query_embedding = embedding_model.encode(prompt).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=1)
    if results["ids"]:
        return results["ids"][0][0]  # Return the best-matching function name
    return None


if __name__ == "__main__":
    print(retrieve_best_function("Launch Google Chrome"))  # Expected: "open_chrome"
    print(retrieve_best_function("Check CPU usage"))  # Expected: "get_cpu_usage"
