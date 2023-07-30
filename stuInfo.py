class Student:
    def __init__(self, rollNo, name, grade, marks):
        self.rollNo = rollNo
        self.name = name
        self.grade = grade
        self.marks = marks

    def __str__(self):
        return f'Roll No: {self.rollNo}\nName: {self.name}\nGrade: {self.grade}\nMarks: {self.marks}\n'

    def changeMarks(self, marks):
        self.marks = marks

    def gradeUp(self):
        self.grade = self.grade + 1

    def changeName(self, newName):
        assert newName != "", "Name can't be empty"
        self.name = newName

student = Student("229", "Meow", "2nd Year", "100")
print(student)

# ch = 1
# while (ch):
#     print("1. Add student")
#     print("2. Get Student Info")
#     print("3. Change Student Name")
#     print("4. Change Marks")
#     print("5. Grade up a student")

#     ch = int(input("Enter: "))

#     if (ch == 1):
#         rollNo = int(input("Enter "))