import ctypes
from AutoInstallDependencies import AutoInstallDependencies
from WhisperParameters import WhisperParameters

# Check dependencies first
AutoInstallDependencies.check_dependencies()

# Import after verification
import customtkinter as customtkinter
from customtkinter import filedialog    

# Sets default model parameters
whisper = WhisperParameters()

# Label widget - Inner window workings
root = customtkinter.CTk()
root.title("Advanced Whisper Interface")

# Inside the window
myLabel = customtkinter.CTkLabel(root, text="Advanced Whisper Interface", font=("Arial", 24))
myLabel.pack(pady=15)  # Add some padding

fileList = []

# Choose files to convert
def selectFile():
    filename = filedialog.askopenfilenames()
    fileList.clear()
    fileList.extend(filename)
    
    fileCount = 0
    for file in fileList:
        fileCount += 1
        print(f"File {fileCount}: " + file)
    print()

def selectFolder():
    outputFolder = filedialog.askdirectory()
    whisper.setOutputPath(outputFolder)

fileSelectButton = customtkinter.CTkButton(root, text = "Select File(s)", command=selectFile)
fileSelectButton.pack(pady=5)
folderSelectButton = customtkinter.CTkButton(root, text = "Select Folder", command=selectFolder)
folderSelectButton.pack(pady=5)

#Select language
languageLabel = customtkinter.CTkLabel(root, text="Language", font=("Arial", 14))
languageLabel.pack()

def language_choice(choice):
    whisper.setLanguage(choice)
language_var = customtkinter.StringVar(value="English")
# language_choice = "English"
customtkinter.CTkLabel(root, text="Output Format", font=("Arial", 14))

supported_languages = ["English", "Spanish", "French", "Afrikaans", "Arabic", "Armenian", "Azerbaijani", "Belarusian",
                        "Bosnian", "Bulgarian", "Catalan", "Chinese", "Croatian", "Czech", "Danish", "Dutch", "English",
                        "Estonian", "Finnish", "French", "Galician", "German", "Greek", "Hebrew", "Hindi", "Hungarian", 
                        "Icelandic", "Indonesian", "Italian", "Japanese", "Kannada", "Kazakh", "Korean", 
                        "Latvian", "Lithuanian", "Macedonian", "Malay", "Marathi", "Maori", "Nepali", "Norwegian", 
                        "Persian", "Polish", "Portuguese", "Romanian", "Russian", "Serbian", "Slovak", "Slovenian", 
                        "Spanish", "Swahili", "Swedish", "Tagalog", "Tamil", "Thai", "Turkish", "Ukrainian", 
                        "Urdu", "Vietnamese", "Welsh"]

languageBox = customtkinter.CTkComboBox(root, values=supported_languages,
                                            command = language_choice, variable=language_var)
languageBox.pack(pady=5)

def model_choice(choice):
    whisper.setModelSize(choice)

    if whisper.getModelSize() == "tiny" or whisper.getModelSize() == "base" or whisper.getModelSize() == "small" or whisper.getModelSize() == "medium":
        language_var.set("English")  # Set the language variable to English
        languageBox.set("English")   # Set the combobox text to English
        languageBox.configure(state="disabled")
    else:
        languageBox.configure(state="normal")

# Lists Options of Models with VRAM sizes, english only models
model_var = customtkinter.StringVar(value="Model (VRAM)")
modelLabel = customtkinter.CTkLabel(root, text="Model Selection", font=("Arial", 14))
modelLabel.pack()  # Add some padding

# Create the combobox
modelSelectBox = customtkinter.CTkComboBox(root, values=["Tiny (En, fast; 1gb)", "Base (1gb, En)", "Small (2gb, En)", "Medium (5gb, En)", "Large (10gb)", "Turbo (Fast, 6gb)"],
                                            command=model_choice, variable=model_var)
modelSelectBox.pack(pady=5)

# Output Format Selection
formatLabel = customtkinter.CTkLabel(root, text="Output Format", font=("Arial", 14))
formatLabel.pack()

# Create variable to track selection
outputFormat_var = customtkinter.StringVar(value="ALL")

# Create radio buttons for each format
def outputFormat_choice(choice):
    whisper.setOutputFormat(choice)
outputFormat_var = customtkinter.StringVar(value="txt")
# outputFormat_choice = "txt"
customtkinter.CTkLabel(root, text="Output Format", font=("Arial", 14))

outputFormatBox = customtkinter.CTkComboBox(root, values=["ALL", "txt", "srt", "json", "vtt", "tsv"],
                                            command = outputFormat_choice, variable=outputFormat_var)

outputFormatBox.pack(pady=5)

def wordTimestamp_choice():
    whisper.setWordTimestamps(wordTimestamp_var.get())
    wordTimestamp_dialog_user_choice()

wordTimestamp_var = customtkinter.StringVar(value="False")
wordTimestampCheckbox = customtkinter.CTkCheckBox(root, text="Word Timestamps", command=wordTimestamp_choice,
                                                    variable = wordTimestamp_var, onvalue="True", offvalue="False")
# Pushes timestamp checkbox to the screen
wordTimestampCheckbox.pack(pady=5)

def wordTimestamp_dialog_user_choice():
    # show a wordTimestamp dialog for selecting a number of words per line
    if wordTimestamp_var.get() == "True":
        # Open input dialog when checkbox is checked
        dialog = customtkinter.CTkInputDialog(text="1, 3, etc.", title="Enter Max # Words Per Line:")
        user_input = dialog.get_input()

        # Checks if user input is a String with at least one digit
        if user_input and user_input.isdigit():
            whisper.setMaxWordsPerLine(user_input)

        elif user_input is None:
            wordTimestamp_var.set("False")
            whisper.setWordTimestamps(wordTimestamp_var.get())

        else:
            ctypes.windll.user32.MessageBoxW(0, f"Enter a valid Number", u"Error", 0)
            wordTimestamp_var.set("False")
            whisper.setWordTimestamps(wordTimestamp_var.get())

def generateButton():

    if(len(fileList) > 0):
        print("Generating Text from Media...\n")
    
        countFiles = 0
        for file in fileList:
            countFiles += 1
            print(f"File #{countFiles}: {file} is being processed...")
            whisper.commandToRun(file)
    else:
        ctypes.windll.user32.MessageBoxW(0, u"Please select at least one file.", u"Error", 0)
        return
    
createTasks = customtkinter.CTkButton(root, text = "Generate Text from Media", command=generateButton)
createTasks.pack(pady=5)

# Loop back through
root.mainloop()