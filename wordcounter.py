#trying to split each line into its individual words and create a full list of words used.
#Make the list

#inFile = input("Where is the file you'd like to analyze?")
#outFile = input('Which file do you want to append to?')

inFile = open("KeywordSearching.txt", 'r')
outFile = open("E:\Program Files\Repos\WordCounter\masterdocs\master.txt", 'a')
inData = inFile.read()
inFile.close()
outData = outFile.write(inData.upper())
outFile.close()

keywords = open('E:\Program Files\Repos\WordCounter\masterdocs\master.txt').readlines()
keywords.sort()
print('Sorted list: ', keywords)


####Current problem? How to get rid of all the '\n'