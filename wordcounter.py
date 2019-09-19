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
doc = open("masterdocs/master.txt", 'r')

d = dict()
for line in doc:
    if line not in d:
        d[line] = 1
    else:
        d[line] = d[line] + 1

print(d)


# keywords = open('masterdocs/master.txt').readlines()
# keywords.sort()
# print('Sorted list: ', keywords)

####Current problem? How to get rid of all the '\n'
