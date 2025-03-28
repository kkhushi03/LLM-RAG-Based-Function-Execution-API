TEMPLATE = """from automation_functions import {function_name}

def main():
    try:
        {function_call}
        print("{success_message}")
    except Exception as e:
        print(f"Error executing function: {e}")

if __name__ == "__main__":
    main()
"""

def generate_code(function_name):
    function_call = f"{function_name}()" if function_name not in ["run_shell_command"] else f'{function_name}("echo Hello")'
    success_message = f"{function_name} executed successfully."

    return TEMPLATE.format(function_name=function_name, function_call=function_call, success_message=success_message)
