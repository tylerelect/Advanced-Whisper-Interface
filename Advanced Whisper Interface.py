import time
import os  # Ensure this is imported at the top
from AutoInstallDependencies import AutoInstallDependencies
from WhisperParameters import WhisperParameters
from WarningDialog import WarningDialog

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
myLabel.pack(padx = 15, pady=15)  # Add some padding

fileList = []

# Choose files to convert
def selectFile():
    # Use filetypes to filter allowed extensions in the file dialog
    filename = filedialog.askopenfilenames(
        title="Select Media Files",
        filetypes=[
            ("Media", "*.mp3 *.wav *.flac *.ogg *.opus *.m4a *.aac *.wma *.m4b *.mpga *.mp4 *.webm *.mkv *.mov *.avi *.mpeg *.ts")]
    )
    fileList.clear()
    fileList.extend(filename)

    fileCount = 0
    for file in fileList:
        fileCount += 1
        print(f"File {fileCount}: {file}")

def selectFolder():
    outputFolder = filedialog.askdirectory()
    whisper.setOutputPath(outputFolder)

fileSelectButton = customtkinter.CTkButton(root, text = "Select File(s)", command=selectFile)
fileSelectButton.pack(pady=5)
folderSelectButton = customtkinter.CTkButton(root, text = "Output Folder", command=selectFolder)
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
            wordTimestamp_var.set("False")
            whisper.setWordTimestamps(wordTimestamp_var.get())
            warning_dialog = WarningDialog(title="Error", label_text="Enter a valid number.")
            warning_dialog.mainloop()      

def generateButton():
    if len(fileList) > 0:
        print("Generating Text from Media...\n")
        
        # Disable the button to prevent multiple clicks
        createTasks.configure(state="disabled")
        
        # Start global timing
        global_start = time.time()

        countFiles = 0
        successful_files = []
        failed_files = []

        # Get the selected output format
        output_format = whisper.getOutputFormat().lower()

        for file in fileList:
            countFiles += 1
            print(f"File #{countFiles}: {file} is being processed...")

            # Start timing for individual file
            start_time = time.time()

            whisper.commandToRun(file)

            # Determine the expected output file based on the selected format
            base_name = os.path.splitext(os.path.basename(file))[0]  # Get the file name without extension

            # If output format is "ALL," random check for a .txt file
            if output_format.lower() == "all":
                output_file = os.path.join(whisper.getOutputPath(), f"{base_name}.txt")
            else:
                output_file = os.path.join(whisper.getOutputPath(), f"{base_name}.{output_format}")

            # Check if the output file exists
            if os.path.exists(output_file):
                successful_files.append(file)
            else:
                failed_files.append(file)

            # End timing for individual file
            end_time = time.time()
            elapsed = end_time - start_time

            print(f"Transcription for File #{countFiles} completed in {elapsed:.2f} seconds.\n")

            # Optional delay for VRAM to clear
            if whisper.getGpuUsage() == "True":
                print("Waiting 5 seconds to allow GPU memory to clear...")
                time.sleep(5)

        # End global timing
        global_end = time.time()
        total_time = global_end - global_start

        # Show results in a warning dialog
        result_message = f"Results:\n\n"
        if successful_files:
            result_message += f"✅Successful Files ({len(successful_files)}):\n" + "\n".join(successful_files) + "\n\n"
        if failed_files:
            result_message += f"❌Failed Files ({len(failed_files)}):\n" + "\n".join(failed_files)

        # Include total time for all files
        minutes, seconds = divmod(total_time, 60)
        result_message += f"\n\nTotal Time: {int(minutes)} minutes and {seconds:.2f} seconds."

        # Close after clicking "Ok"
        def close_program():
            root.destroy()
            warning_dialog.destroy()

        warning_dialog = WarningDialog(title="Transcription Results", label_text=result_message, largewindow=True)
        warning_dialog.ok_button.configure(command=close_program)
        warning_dialog.mainloop()
    else:
        warning_dialog = WarningDialog(title="Error", label_text="Please select at least one file.")
        warning_dialog.mainloop()

createTasks = customtkinter.CTkButton(root, text="Generate Text from Media", command=generateButton)
createTasks.pack(pady=5)

# Loop back through
root.mainloop()