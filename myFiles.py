import pickle

def writeIntoFile():
    myFile = open("mist.dat", "ab")
    ch = 'Y'
    while ch == 'Y':
        D = {}
        rno = int(input("Enter Roll Number"))
        name = input("Enter Name")
        marks = float(input("Enter Marks"))

        D["RollNo"] = rno
        D["Name"] = name
        D["Marks"] = marks

        pickle.dump(D, myFile)

        ch = input("Want to add more")
    myFile.close()

def readFile():
    myFile = open("mist.dat", "rb")
    print("\nFile Data:\n")
    try:
        while True:
            record = pickle.load(myFile)
            print(record)
    except EOFError:
        myFile.close()

def searchInFile():
    myFile = open("mist.dat", "rb")
    # for marks greater than 96

    try:
        while True:
            D = pickle.load(myFile)
            if D["Marks"] > 96:
                print(D)
    except EOFError:
        myFile.close()
    

def modifyFile():
    myFile = open("mist.dat", "rb+")

    try:
        while True:
            pointer = myFile.tell()

            D = pickle.load(myFile)

            if (D["Marks"] < 90):
                D["Marks"] += 5
                myFile.seek(pointer)
                pickle.dump(D, myFile)
    except EOFError:
        myFile.close()


# writeIntoFile()
# searchInFile()
readFile()
modifyFile()
readFile()