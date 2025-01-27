import subprocess
import sys

def create_executable(script_name):
    # Prepare the PyInstaller command
    command = [
        "PyInstaller",  # PyInstaller executable
        "--onefile",    # Option to generate a single executable file
        script_name     # The script name (e.g., your_script.py)
    ]

    # Run the command and capture the output
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the process completed successfully
    if result.returncode == 0:
        print(f"Executable created successfully: {script_name}")
    else:
        print(f"Error occurred while creating the executable:\n{result.stderr}")

# Ensure this is run when the script is executed directly
if __name__ == "__main__":
    # Provide the name of the script you want to convert to .exe
    script_name = "C:\\Users\\AgamSafaruddinDeutsc\\Documents\\Projekt\\autoausfueller\\app.py"  # Replace with the script you want to convert
    create_executable(script_name)
