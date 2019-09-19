# inFile = input("Where is the file you'd like to analyze?")
# outFile = input('Which file do you want to append to?')

# Copies keywordsearching to master. Allows for manipulation while retaining original file

inFile = open("KeywordSearching.txt", 'r')
outFile = open("masterdocs/master.txt", 'a')
inData = inFile.read()
inFile.close()
outData = outFile.write(inData.upper())
outFile.close()

# let's try a dictionary?

d = {}
with open('masterdocs/master.txt') as keyword:
    for line in keyword:
        word = line.strip('\n')
        d[word]
print(d)

# keywords = open('masterdocs/master.txt').readlines()
# keywords.sort()
# print('Sorted list: ', keywords)

####Current problem? How to get rid of all the '\n'
