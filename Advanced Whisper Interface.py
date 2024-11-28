from AutoInstallDependencies import AutoInstallDependencies
from WhisperParameters import WhisperParameters

# Check dependencies first
AutoInstallDependencies.check_dependencies()

# Import after verification
import customtkinter as customtkinter

# Sets default model parameters
whisper = WhisperParameters()

# Label widget - Inner window workings
root = customtkinter.CTk()
root.title("Advanced Whisper Interface")

# Inside the window
myLabel = customtkinter.CTkLabel(root, text="Advanced Whisper Interface", font=("Arial", 24))
myLabel.pack(pady=20)  # Add some padding

def model_choice(choice):
    whisper.setModelSize(choice)

# Lists Options of Models with VRAM sizes, english only models
model_var = customtkinter.StringVar(value="Model (VRAM)")
combobox = customtkinter.CTkComboBox(root, values=["Tiny (En, fast; 1gb)", "Base (1gb, En)", "Small (2gb, En)", "Medium (5gb, En)", "Large (10gb)", "Turbo (Fast, 6gb)"],
                                     command=model_choice, variable=model_var)

modelSelection = customtkinter.CTkButton(root, text = "button")

#push onto screen
myLabel.pack()
combobox.pack()
modelSelection.pack()

# Loop back through
root.mainloop()