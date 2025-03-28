from fastapi import FastAPI, HTTPException
from vector_store import retrieve_function
from code_generator import generate_code
import automation_functions as af

app = FastAPI()

@app.post("/execute")
def execute_function(request: dict):
    user_prompt = request.get("prompt", "").strip()

    if not user_prompt:
        raise HTTPException(status_code=400, detail="Prompt is required.")

    function_name = retrieve_function(user_prompt)

    if not function_name or function_name not in af.FUNCTIONS:
        raise HTTPException(status_code=404, detail="Function not found.")

    generated_code = generate_code(function_name)
    try:
        result = af.FUNCTIONS[function_name]() if callable(af.FUNCTIONS[function_name]) else "Function executed"
    except Exception as e:
        result = str(e)

    return {
        "function": function_name,
        "code": generated_code,
        "execution_result": result
    }

# Run the API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
