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
outputFormat_var = customtkinter.StringVar(value="ALL")

# make array?? checkbox?!
# Create radio buttons for each format

def outputFormat_choice(choice):
    whisper.setOutputFormat(choice)
outputFormat_choice = "txt"
customtkinter.CTkLabel(root, text="Output Format", font=("Arial", 14))

outputFormatBox = customtkinter.CTkComboBox(root, values=["All", "txt", "srt", "json", "vtt", "tsv"],
                                     command=outputFormat_choice, variable=outputFormat_choice)

outputFormatBox.pack(pady=5)

allRadio = customtkinter.CTkRadioButton(root, text="ALL", variable=outputFormat_var, value="ALL",
                                       command=lambda: whisper.setOutputFormat(outputFormat_var.get()))

txtRadio = customtkinter.CTkRadioButton(root, text="TXT", variable=outputFormat_var, value="txt", 
                                       command=lambda: whisper.setOutputFormat(outputFormat_var.get()))

srtRadio = customtkinter.CTkRadioButton(root, text="SRT", variable=outputFormat_var, value="srt",
                                       command=lambda: whisper.setOutputFormat(outputFormat_var.get()))

jsonRadio = customtkinter.CTkRadioButton(root, text="JSON", variable=outputFormat_var, value="json",
                                       command=lambda: whisper.setOutputFormat(outputFormat_var.get()))

vttRadio = customtkinter.CTkRadioButton(root, text="VTT", variable=outputFormat_var, value="vtt",
                                       command=lambda: whisper.setOutputFormat(outputFormat_var.get()))

tsvRadio = customtkinter.CTkRadioButton(root, text="TSV", variable=outputFormat_var, value="tsv",
                                       command=lambda: whisper.setOutputFormat(outputFormat_var.get()))

# Pack the radio buttons
allRadio.pack(pady=2)
txtRadio.pack(pady=2)
srtRadio.pack(pady=2)
jsonRadio.pack(pady=2)
vttRadio.pack(pady=2)
tsvRadio.pack(pady=2)

#push onto screen
myLabel.pack()
modelSelection.pack()
modelSelectBox.pack()

# Loop back through
root.mainloop()