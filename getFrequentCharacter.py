def getFrequentCharactersFromFile(fileName):
    myFile = open(f"{fileName}.txt", "r")

    dict = {}
    maxFrequency = 0
    mostFrequentCharacters = []

    for line in myFile:
        text = line.strip("\n")
        for char in text:
            if (char == " " or char == "," or char == ";"):
                continue
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
            maxFrequency = max(maxFrequency, dict[char])

    for i in dict:
        print(i, dict[i])
        if dict[i] == maxFrequency:
            mostFrequentCharacters.append(i)
    print(mostFrequentCharacters)

getFrequentCharactersFromFile("DSC")