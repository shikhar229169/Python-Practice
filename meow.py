def writeIntoFile():
    myFile = open("mist.txt", "a")

    N = int(input("Enter number of lines u want to write: "))
    for i in range(N):
        currLine = input(f'Enter line {i+1}')
        myFile.write(currLine)
        myFile.write("\n")
    
    myFile.close()

def readFromFile():
    myFile = open("mist.txt", "r")
    # for i in myFile:
    #     print(i, end = "")

    while True:
        line = myFile.readline()
        if not line:
            break
        print(line)
    
    myFile.close()

def readFromFile_():
    with open("mist.txt", "r") as myFile:
        content = myFile.read()
        print(content)
        # for i in myFile:
        #     print(i, end = "")

readFromFile_()