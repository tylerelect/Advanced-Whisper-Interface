# Defines the parameters using accessors and mutator methods

# TODO: create original variable for large and any other non-english models for referring back to them
class WhisperParameters:
    def __init__(self, language = "English", model = "Medium", outputPath = "%%userprofile%%\Desktop\Advanced Whisper Output", 
                 outputFormat = "txt",
                   wordTimestamps = True, maxWordsPerLine = 1):
        self.language = language
        self.model = model
        self.outputPath = None
        self.outputFormat = outputFormat
        self.wordTimestamps = wordTimestamps
        self.maxWordsPerLine = maxWordsPerLine
    
    def setLanguage(self, language):
        self.language = language
    def getLanguage(self):
        return self.language
    
    def setOutputPath(self, outputPath):
        self.outputPath = outputPath
    def getOutputPath(self):
        return self.outputPath

    def setOutputFormat(self, outputFormat):
        self.outputFormat = outputFormat
        print(self.getOutputFormat())
    def getOutputFormat(self):
        return self.outputFormat

    def setWordTimestamps(self, wordTimestamps):
        self.wordTimestamps = wordTimestamps
    def getWordTimestamps(self):
        return self.wordTimestamps

    def setMaxWordsPerLine(self, maxWordsPerLine):
        self.maxWordsPerLine = maxWordsPerLine
    def getMaxWordsPerLine(self):
        return self.maxWordsPerLine

    # Model Size
    def setModelSize(self, model):
        # Get just the first word of the model name
        word = model.split()[0]
        self.model = word.lower()
    
        # Optional: Check for English model
        if "en" in model.lower():
            self.language = "English"
        
        #Test case
        print(f"Model: {self.model}, Language: {self.language}")
    def getModelSize(self):
        return self.model.lower()

    
    # After the check if model is English only, throws error for other language being selected
