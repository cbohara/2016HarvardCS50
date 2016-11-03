from student import Student

students = []
for i in range(3):
    print("Name: ", end="")
    name = input()
    print("Dorm: ", end="")
    dorm = input()
    students.append(Student(name, dorm))

for student in students:
    print(student.name, end="") + " lives in " + print(student.dorm)
