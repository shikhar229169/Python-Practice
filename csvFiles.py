import csv

def writeFile():
    myFile = open("mist.csv", "w")

    writer = csv.writer(myFile)

    writer.writerow(['RollNo', 'Name', 'Marks'])

    for i in range(3):
        rno = int(input("Enter Roll Number"))
        name = input("Enter Name")
        marks = float(input("Enter Marks"))

        writer.writerow([rno, name, marks])

    myFile.close()


def readFile():
    myFile = open("mist.csv", "r", newline = '\r\n')
    
    reader = csv.reader(myFile)
    for i in reader:
        print(i)
    
    myFile.close()



writeFile()
readFile()