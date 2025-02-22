import ctypes
from CheckCudaCapability import check_gpu_status_once

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
            ctypes.windll.user32.MessageBoxW(0, u"Selected model only supports English. Defaulting to English", u"Error with selected model", 0)
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
        # self.maxWordsPerLine = "{}".format(self.maxWordsPerLine)
        return self.maxWordsPerLine

    # Model Size
    def setModelSize(self, model):
        # Get just the first word of the model name
        self.model = model.split()[0].lower()

        # Default to English when model does not support other languages
        if self.getModelSize() == "tiny" or self.getModelSize() == "base" or self.getModelSize() == "small" or self.getModelSize() == "medium":
            print("okay the top of the method works")
            if self.getLanguage() != "English":
                ctypes.windll.user32.MessageBoxW(0, u"Selected model only supports English. Defaulting to English. Press ok to continue.", u"Error with selected language", 0)
                self.language = "English"
            
        #Test case
        print(f"Model: {self.model}, Language: {self.language}")

    def getModelSize(self):
        return self.model.lower()
    
    def getGpuUsage(self):
        return self.gpu
    
    def commandToRun(self, currentFile):

        if(self.outputPath is not None):
            print("Language: " + self.language + 
                    "\nModel: " + self.model +
                    "\nOutput Format: " + self.outputFormat +
                    "\nWord Timestamps: " + self.wordTimestamps +
                    "\nMax Words Per Line: " + self.maxWordsPerLine +
                    "\nOutput Path: " + self.outputPath )
        else:
            ctypes.windll.user32.MessageBoxW(0, u"Please select an output folder.", u"Error", 0)
            return
    