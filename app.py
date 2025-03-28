from fastapi import FastAPI
import json

app = FastAPI()

function_registry = {
    "open_chrome": "from automation_functions import open_chrome\n\ndef main():\n    try:\n        print(\"Execution successful.\")\n    except Exception as e:\n        print(f\"Error executing function: {e}\")\n\nif __name__ == \"__main__\":\n    main()\n"
}

@app.post("/execute")
async def execute(request: dict):
    prompt = request.get("prompt", "").lower()
    
    # Map prompt to function name
    if "chrome" in prompt:
        function_name = "open_chrome"
    else:
        return {"error": "Function not found"}

    # Retrieve function code (DO NOT EXECUTE)
    function_code = function_registry.get(function_name)
    if function_code:
        return {"function": function_name, "code": function_code, "output": None}
    else:
        return {"error": "Function not available"}
