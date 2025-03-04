import tkinter as tk
from tkinter import filedialog

def select_file():
    # Open a file dialog to choose a text file
    file_path = filedialog.askopenfilename(
        title="Select a Text File",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    
    if file_path:  # If a file was selected
        print(f"Full file path: {file_path}")

        # Get just the file name (without the path)
        file_name = file_path.split("/")[-1]
        print(f"Selected file name: {file_name}")

        # Open and read the contents of the file
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                print("\nFile content:")
                print(content)
        except Exception as e:
            print(f"Error reading the file: {e}")

# Create a simple Tkinter window
root = tk.Tk()
root.withdraw()  # Hide the root window

select_file()
