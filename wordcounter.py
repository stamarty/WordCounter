# Copies text file to master.
# Allows for manipulation while retaining original file

hFile = input("Where is the file you'd like to analyze? ")
inFile = open(hFile, 'r')
outFile = open("masterdocs/master.txt", 'w')
inData = inFile.read()
inFile.close()
outData = outFile.write(inData.upper())
outFile.close()

# opens master.txt for manipulation
try:
    doc = open("masterdocs/master.txt", 'r')
except:
    print('File cannot be opened: ', doc)
    quit()

# Create dictionary and count the words
d = dict()
for line in doc:
    line = line.strip()
    if line not in d:
        d[line] = 1
    else:
        d[line] = d[line] + 1

# sort by value instead of key
print(sorted([(v, k) for k, v in d.items()], reverse=True))
