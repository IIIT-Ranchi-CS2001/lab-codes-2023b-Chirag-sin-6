n=int(input("Enter the number of students: "))
names = [input(f"Enter the name of student {i+1}: ") for i in range(n)]
roll_nos = [int(input(f"Enter the roll number of student {i+1}: ")) for i in range(n)]
marks = [float(input(f"Enter the marks in Physics of student {i+1}: ")) for i in range(n)]

students = [(names[i], roll_nos[i], marks[i]) for i in range(n)]

for i in range(len(students)):
    for j in range(i + 1, len(students)):
            students[i], students[j] = students[j], students[i]  

print("Sorted list of students by marks:")
for student in students:
    print(student)
