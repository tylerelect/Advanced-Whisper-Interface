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
myLabel.pack(pady=15)  # Add some padding

def model_choice(choice):
    whisper.setModelSize(choice)

# Lists Options of Models with VRAM sizes, english only models
model_var = customtkinter.StringVar(value="Model (VRAM)")
modelLabel = customtkinter.CTkLabel(root, text="Model Selection", font=("Arial", 14))
modelLabel.pack()  # Add some padding

# Create the combobox
modelSelectBox = customtkinter.CTkComboBox(root, values=["Tiny (En, fast; 1gb)", "Base (1gb, En)", "Small (2gb, En)", "Medium (5gb, En)", "Large (10gb)", "Turbo (Fast, 6gb)"],
                                     command=model_choice, variable=model_var)
modelSelectBox.pack(pady=5)

modelSelection = customtkinter.CTkButton(root, text = "finalize")

# After the model selection elements, add:

# Output Format Selection
formatLabel = customtkinter.CTkLabel(root, text="Output Format", font=("Arial", 14))
formatLabel.pack()

# Create variable to track selection
format_var = customtkinter.StringVar(value="txt")

# make array?? checkbox?!
# Create radio buttons for each format
txtRadio = customtkinter.CTkRadioButton(root, text="TXT", variable=format_var, value="txt", 
                                       command=lambda: whisper.setOutputFormat(format_var.get()))
srtRadio = customtkinter.CTkRadioButton(root, text="SRT", variable=format_var, value="srt",
                                       command=lambda: whisper.setOutputFormat(format_var.get()))
vttRadio = customtkinter.CTkRadioButton(root, text="VTT", variable=format_var, value="vtt",
                                       command=lambda: whisper.setOutputFormat(format_var.get()))

# Pack the radio buttons
txtRadio.pack(pady=2)
srtRadio.pack(pady=2)
vttRadio.pack(pady=2)

#push onto screen
myLabel.pack()
modelSelection.pack()
modelSelectBox.pack()

# Loop back through
root.mainloop()