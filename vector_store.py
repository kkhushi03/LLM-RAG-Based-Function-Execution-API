import chromadb
from sentence_transformers import SentenceTransformer

# Initialize vector DB and embedding model
chroma_client = chromadb.PersistentClient(path="./vector_db")
collection = chroma_client.get_or_create_collection(name="function_store")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Function descriptions (metadata)
function_metadata = {
    "open_chrome": "Launch Google Chrome",
    "open_calculator": "Open the calculator application",
    "open_notepad": "Launch Notepad for text editing",
    "get_cpu_usage": "Retrieve current CPU usage",
    "get_ram_usage": "Check RAM usage percentage",
    "run_shell_command": "Execute a shell command"
}

# Populate vector DB
def populate_vector_db():
    for func_name, description in function_metadata.items():
        embedding = model.encode(description).tolist()
        collection.add(ids=[func_name], embeddings=[embedding], metadatas=[{"description": description}])

# Retrieve best matching function
def retrieve_function(user_prompt):
    query_embedding = model.encode(user_prompt).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=1)
    if results["ids"]:
        return results["ids"][0][0]
    return None

# Initialize database
populate_vector_db()
