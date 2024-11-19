import importlib.util
import sys
import subprocess

def check_dependencies():
    required_packages = ['customtkinter', 'whisper']
    
    for package in required_packages:
        if importlib.util.find_spec(package) is None:
            print (f"\nRequired package '{package}' is not installed. Installing...\n")
            install_package(package)

def install_package(package_name):
    """
    Installs a package using pip within the current environment.
    """
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package_name}. Error: {e}")


# Check dependencies first
check_dependencies()

# Import after verification
import customtkinter as ctk

# Label widget - Inner window workings
root = ctk.CTk()
root.title("Advanced Whisper Interface")

# Inside the window
myLabel = ctk.CTkLabel(root, text="Advanced Whisper Interface", font=("Arial", 24))
myLabel.pack(pady=20)  # Add some padding

modelSelection = ctk.CTkButton(root, text = "medium")

#push onto screen
myLabel.pack()
modelSelection.pack()

# Loop back through
root.mainloop()