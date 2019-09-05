
#Change these to inputs values for final.
f = open("C:/Users/Steven.Martinez/source/repos/WordCounter/KeywordSearching.txt")

## trying to split each line into its individual words and create a full list of words used.
lines = dict()
for line in lines:
    words = line.split()
    for word in words:

masterDoc = open("C:/Users/Steven.Martinez/source/repos/WordCounter/masterdocs/master.txt", "w")
masterDoc.write("yay!")

for x in f:
    x.lower()
    x.split()
    x.write(masterDoc, "a")
    print(x)

f.close()
masterDoc.close()