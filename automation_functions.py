import os
import webbrowser
import psutil
import subprocess

def open_chrome():
    webbrowser.open("https://www.google.com")

def open_calculator():
    os.system("calc")

def open_notepad():
    os.system("notepad")

def get_cpu_usage():
    return f"CPU Usage: {psutil.cpu_percent()}%"

def get_ram_usage():
    return f"RAM Usage: {psutil.virtual_memory().percent}%"

def run_shell_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else result.stderr

FUNCTIONS = {
    "open_chrome": open_chrome,
    "open_calculator": open_calculator,
    "open_notepad": open_notepad,
    "get_cpu_usage": get_cpu_usage,
    "get_ram_usage": get_ram_usage,
    "run_shell_command": run_shell_command
}

if __name__ == "__main__":
    open_calculator()  # Should open the calculator
    print(get_cpu_usage())  # Should print CPU usage
