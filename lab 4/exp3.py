CourseCode=["CS1001","MA2001","CS2005"]
CourseName=["Python","Maths","COA"]

list=[]
for i in range(len(CourseCode)):
    list.append((f"{CourseCode[i]}:{CourseName[i]} "))

print(list)
