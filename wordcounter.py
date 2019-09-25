# Copies text file to master.
# Allows for manipulation while retaining original file
class WordCounter: 

    def __init__(self, filename, *args, **kwargs):
        self._filename = filename
        return super().__init__(*args, **kwargs)
    
    def promptUserForFile(self):
        userFilePath = input("Where is the file you'd like to analyze? ")
        userFile = open(userFilePath, 'r')
        outFile = open(self._filename, 'w')
        inData = userFile.read()
        userFile.close()
        outData = outFile.write(inData.upper())
        outFile.close()

    def openFile(self):
        try:
            self._doc = open(self._filename, 'r')
        except:
            print('File cannot be opened: ', doc)
            quit()
    
    def countWordsAndSort(self):
        self.countWords()
        self.sortWordsByValue()
            
    def countWords(self):
        self._d = dict()
        for line in self._doc:
            line = line.strip()
            if line not in self._d:
                self._d[line] = 1
            else:
                self._d[line] = self._d[line] + 1

    def sortWordsByValue(self):
        self._sortedWords = sorted([(v, k) for k, v in self._d.items()], reverse=True)
        
    def printWords(self):
        for k,v in self._sortedWords:
            print(f"{k} : {v}")



wordCounter = WordCounter("masterdocs/master.txt")
wordCounter.promptUserForFile()
wordCounter.openFile()
wordCounter.countWordsAndSort()
wordCounter.printWords()

