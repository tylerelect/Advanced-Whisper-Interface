import shlex

import torch
from CheckCudaCapability import check_gpu_status_once
from WarningDialog import WarningDialog
import subprocess

# Defines the parameters using accessors and mutator methods

# TODO: create original variable for large and any other non-english models for referring back to them
class WhisperParameters:
    def __init__(self, language = "English", model = "Medium",
                 outputPath = "%%userprofile%%\Desktop\Advanced Whisper Output", 
                 outputFormat = "txt", wordTimestamps = "False", maxWordsPerLine = str(1)):
        self.language = language
        self.model = model
        self.outputPath = None
        self.outputFormat = outputFormat
        self.wordTimestamps = wordTimestamps
        self.maxWordsPerLine = maxWordsPerLine
        self.gpu = check_gpu_status_once()
    
    # Set the language of the model to transcribe
    def setLanguage(self, language):
        if "en" in self.model.lower():
            warning_dialog = WarningDialog(title="Error with selected model", label_text="Selected model only supports English. Defaulting to English")
            warning_dialog.mainloop()
            self.language = "English"
        else:
            self.language = language

        print("Language: " + self.getLanguage())

    def getLanguage(self):
        return self.language
    
    def setOutputPath(self, outputPath):
        self.outputPath = outputPath
    def getOutputPath(self):
        return self.outputPath
    
    # def setCustomFileName(self, name):
    #     self.outputPath = os.path.join(self.outputPath, name)

    def setOutputFormat(self, outputFormat):
        self.outputFormat = outputFormat
        print(self.getOutputFormat())
        
    def getOutputFormat(self):
        return self.outputFormat

    def setWordTimestamps(self, wordTimestamps):
        self.wordTimestamps = wordTimestamps
        print("word timestamps value is: " + self.getWordTimestamps())

    def getWordTimestamps(self):
        return self.wordTimestamps

    def setMaxWordsPerLine(self, maxWordsPerLine):
        self.maxWordsPerLine = maxWordsPerLine
        print("Max words per line: " + self.getMaxWordsPerLine())
    def getMaxWordsPerLine(self):
        return self.maxWordsPerLine

    # Model Size
    def setModelSize(self, model):
        # Get just the first word of the model name
        self.model = model.split()[0].lower()

        # Default to English when model does not support other languages
        if self.getModelSize() == "tiny" or self.getModelSize() == "base" or self.getModelSize() == "small" or self.getModelSize() == "medium":
            print("okay the top of the method works")
            if self.getLanguage() != "English":
                warning_dialog = WarningDialog(title="Selected Language Error", label_text="Selected model only supports English. Defaulting to English. Press ok to continue.")
                warning_dialog.mainloop()
                self.language = "English"
            
        #Test case
        print(f"Model: {self.model}, Language: {self.language}")

    def getModelSize(self):
        return self.model.lower()
    
    def getGpuUsage(self):
        return self.gpu
    
    def commandToRun(self, currentFile):
        if not self.outputPath:
            warning_dialog = WarningDialog(title="Output Error", label_text="Please select an output folder.")
            warning_dialog.mainloop()
            return

        print("Language: " + self.getLanguage() + 
            "\nModel: " + self.getModelSize() +
            "\nOutput Format: " + self.getOutputFormat() +
            "\nWord Timestamps: " + self.getWordTimestamps() +
            "\nMax Words Per Line: " + str(self.getMaxWordsPerLine()) +
            "\nOutput Path: " + self.outputPath)

        # Build the command to run Whisper
        cmd = [
            "whisper",
            currentFile,
            "--device", "cuda" if self.getGpuUsage() else "cpu",
            "--model", self.getModelSize(),
            "--output_dir", self.getOutputPath()
        ]

        if self.getOutputFormat().lower() != "all":
            cmd.extend(["--output_format", self.getOutputFormat()])

        if self.language != "English":
            cmd.extend(["--language", self.getLanguage()])
        else :
            cmd.extend(["--language", "English"])

        if str(self.wordTimestamps).lower() == "true":
            cmd.extend(["--word_timestamps", "True"])
            cmd.extend(["--max_words_per_line", str(self.getMaxWordsPerLine())])

        # Safely quote the command
        safe_cmd = " ".join(shlex.quote(part) for part in cmd)
        print(f"Running: {safe_cmd}")

    
        print("Using GPU:", torch.cuda.is_available())
        print("GPU name:", torch.cuda.get_device_name(0))
        process = subprocess.Popen(
            f'start /wait powershell.exe -Command {safe_cmd}', #add NoExit param to keep the window open
            shell=True
        )
        process.wait()