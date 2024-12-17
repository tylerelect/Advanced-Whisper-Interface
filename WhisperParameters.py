import os
import ctypes
from CheckCudaCapability import check_gpu_status

# Defines the parameters using accessors and mutator methods

# TODO: create original variable for large and any other non-english models for referring back to them
class WhisperParameters:
    def __init__(self, language = "English", model = "Medium",
                 outputPath = "%%userprofile%%\Desktop\Advanced Whisper Output", 
                 outputFormat = "txt", wordTimestamps = None, maxWordsPerLine = 1,):
        self.language = language
        self.model = model
        self.outputPath = None
        self.outputFormat = outputFormat
        self.wordTimestamps = wordTimestamps
        self.maxWordsPerLine = maxWordsPerLine
        self.gpu = check_gpu_status()
    
    # Set the language of the model to transcribe
    def setLanguage(self, language):
        if "en" in self.model.lower():
            ctypes.windll.user32.MessageBoxW(0, u"Selected model only supports English. Defaulting to English", u"Error with selected model", 0)
            self.language = "English"
        else:
            self.language = language

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
        print("TEST YAY! USING MAX WORDS PER LINE!!!!")
    def getMaxWordsPerLine(self):
        return self.maxWordsPerLine

    # Model Size
    def setModelSize(self, model):
        # Optional: Check for English model
        if "en" in model.lower():
            self.language = "English"
        
        # Get just the first word of the model name
        self.model = model.split()[0].lower()
            
        #Test case
        print(f"Model: {self.model}, Language: {self.language}")

    def getModelSize(self):
        return self.model.lower()
    
    def getGpuUsage(self):
        return self.gpu
    
    def commandToRun():
        return "whisper "