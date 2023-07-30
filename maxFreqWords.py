file = open("DSC.txt", "r")

dict = {}
maxFreq = 0
reqWords = []

for line in file:
    wordsArr = line.replace("\n", "").replace(".", "").replace(",", "").split(" ")
    for word in wordsArr:
        if (word not in dict):
            dict[word] = 1
        else:
            dict[word] += 1

        maxFreq = max(maxFreq, dict[word])

for i in dict:
    if dict[i] == maxFreq:
        reqWords.append(i)

for i in dict:
    print(f'{i} - {dict[i]}')