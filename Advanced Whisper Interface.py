from AutoInstallDependencies import AutoInstallDependencies
from CommandBuilder import CommandBuilder

# Check dependencies first
AutoInstallDependencies.check_dependencies()

# Import after verification
import customtkinter as customtkinter

# Label widget - Inner window workings
root = customtkinter.CTk()
root.title("Advanced Whisper Interface")

# Inside the window
myLabel = customtkinter.CTkLabel(root, text="Advanced Whisper Interface", font=("Arial", 24))
myLabel.pack(pady=20)  # Add some padding


def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)

combobox_var = customtkinter.StringVar(value="Medium")
# Lists Options of Models with VRAM sizes, english only models
combobox = customtkinter.CTkComboBox(root, values=["Tiny (1gb)", "Base", "Small", "Medium", "Large", "Turbo"],
                                     command=combobox_callback, variable=combobox_var)
combobox_var.set("Medium")

modelSelection = customtkinter.CTkButton(root, text = "button")

#push onto screen
myLabel.pack()
combobox.pack()
modelSelection.pack()

# Loop back through
root.mainloop()