import pickle

def writeIntoFile(N, fileName):
    myFile = open(f"{fileName}.dat", "wb")

    L = ["Name", "Job", "Salary"]
    pickle.dump(L, myFile)

    for i in range(N):
        print(f"------------------------Details for Employee: {i + 1}---------------------------------")
        L = []
        name = input("Enter name: ")
        job = input("Enter Job: ")
        salary = float(input("Enter salary: "))

        L = [name, job, salary]

        pickle.dump(L, myFile)
        
    myFile.close()

def readFromFile(fileName):
    myFile = open(f"{fileName}.dat", "rb")

    try:
        while (True):
            L = pickle.load(myFile)
            print(L)
    except EOFError:
        myFile.close()

'''
@param fileName The name of .dat file which you want to modify
@param increment The percentage of salary to increase
@notice Increments the salary of everyone by percentage specified in increment
'''
def incrementSalaryByPercentage(fileName, increment):
    myFile = open(f"{fileName}.dat", "rb+")

    L = pickle.load(myFile)

    try:
        while (True):
            ptr = myFile.tell()
            L = pickle.load(myFile)
            salary = L[2]
            salary = salary + (salary * increment) / 100
            L[2] = salary
            myFile.seek(ptr)
            pickle.dump(L, myFile)

    except EOFError:
        myFile.close()


# writeIntoFile(3, "employee")
print("--------------------------------------------------")
readFromFile("employee")
print("--------------------------------------------------")
incrementSalaryByPercentage("employee", 5)
readFromFile("employee")