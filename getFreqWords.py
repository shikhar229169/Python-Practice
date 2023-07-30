myFile = open("polygonId.txt", "r")


frequentWord = []
frequency = 0
dict = {}

for line in myFile:
    wordsArr = line.lower().replace('.', ' ').replace(',', ' ').split(" ")
    for word in wordsArr:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

        frequency = max(frequency, dict[word])

for i in dict:
    if (dict[i] == frequency):
        frequentWord.append(i)

print(frequentWord)
print(frequency)