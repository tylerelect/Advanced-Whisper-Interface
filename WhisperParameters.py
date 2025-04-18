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

        print("Language: " + self.language + 
            "\nModel: " + self.model +
            "\nOutput Format: " + self.outputFormat +
            "\nWord Timestamps: " + self.wordTimestamps +
            "\nMax Words Per Line: " + str(self.maxWordsPerLine) +
            "\nOutput Path: " + self.outputPath)

        # Build the whisper command
        cmd = [
            "powershell.exe",
            "whisper",
            f'"{currentFile}"',
            f'--model {self.model}',
            f'--output_format {self.outputFormat}',
            f'--output_dir "{self.outputPath}"'
        ]
        if self.language.lower() != "english":
            cmd.append(f'--language {self.language.lower()}')
        if str(self.wordTimestamps).lower() == "true":
            cmd.append("--word_timestamps")
        if self.maxWordsPerLine:
            cmd.append(f'--max_words_per_line {self.maxWordsPerLine}')
        if self.getGpuUsage():
            cmd.append("--device cuda")

        full_cmd = " ".join(cmd)
        print(f"Running: {full_cmd}")
        subprocess.run(full_cmd, shell=True)