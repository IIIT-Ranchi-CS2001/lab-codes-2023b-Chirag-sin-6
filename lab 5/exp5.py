students = {}

for i in range(5):
    name = input(f"Enter the name of student {i+1}: ")
    marks = float(input(f"Enter the marks (in percentage) of {name}: "))
    students[name] = marks

high_performers = []
average_performers = []
low_performers = []

for name, marks in students.items():
    if marks >= 85:
        high_performers.append(name)
    elif 60 <= marks < 85:
        average_performers.append(name)
    else:
        low_performers.append(name)

print("Classification of students:")
print(f"High Performers: {len(high_performers)} students - {high_performers}")
print(f"Average Performers: {len(average_performers)} students - {average_performers}")
print(f"Low Performers: {len(low_performers)} students - {low_performers}")

top_student = max(students, key=students.get)
print(f"\nThe student with the highest marks is {top_student} with {students[top_student]}% marks.")
