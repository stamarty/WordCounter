
#Change these to inputs values for final.
f = open("C:/Users/Steven.Martinez/source/repos/WordCounter/KeywordSearching.txt")
masterDoc = open("C:/Users/Steven.Martinez/source/repos/WordCounter/masterdocs/master.txt", "w")
masterDoc.write("yay!")

for x in f:
    print(x)

f.close()
masterDoc.close()