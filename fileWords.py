file = open("DSC.txt", "r")

myFile = ""
curr = 0

for line in file:
    myFile += line
    curr = 1

assert curr == 0, "abc"

print(myFile)