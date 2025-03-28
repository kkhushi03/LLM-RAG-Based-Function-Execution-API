def generate_function_code(function_name):
    return f"""from automation_functions import {function_name}

def main():
    try:
        result = {function_name}()
        print("Execution successful.")
        if result:
            print(f"Output: {{result}}")
    except Exception as e:
        print(f"Error executing function: {{e}}")

if __name__ == "__main__":
    main()
    """

if __name__ == "__main__":
    print(generate_function_code("open_chrome"))
