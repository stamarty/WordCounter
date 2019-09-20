# inFile = input("Where is the file you'd like to analyze?")
# outFile = input('Which file do you want to append to?')

# Copies keywordsearching to master. Allows for manipulation while retaining original file

inFile = open("KeywordSearching.txt", 'r')
outFile = open("masterdocs/master.txt", 'a')
inData = inFile.read()
inFile.close()
outData = outFile.write(inData.upper())
outFile.close()

try:
    doc = open("masterdocs/master.txt", 'r')
except:
    print('File cannot be opened: ', doc)
# Dictionary works. All values are in console and counted!
d = dict()
for line in doc:
    line = line.strip()
    if line not in d:
        d[line] = 1
    else:
        d[line] = d[line] + 1

print(d)


# keywords = open('masterdocs/master.txt').readlines()
# keywords.sort()
# print('Sorted list: ', keywords)

####Current problem? How to get rid of all the '\n'
