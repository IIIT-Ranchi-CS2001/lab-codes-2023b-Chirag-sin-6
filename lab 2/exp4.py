Name=input("Enter the name:")
Roll_number=int(input("Enter the Roll Number:"))
Marks=int(input("Enter the Marks:"))

print("Name: ",Name)
print("Roll Number: ",Roll_number)
print("Marks: ",Marks)

if(Marks>=90):
    print("Grade Point: 10")
    print("Remark: Outstanding")

elif(Marks>90 and Marks>=80):
    print("Grade Point: 9")
    print("Remark: Very Good")

elif(Marks>80 and Marks>=70):
    print("Grade Point: 8")
    print("Remark: Good")

elif(Marks>70 and Marks>=60):
    print("Grade Point: 7")
    print("Remark: Average")

elif(Marks>60 and Marks>=50):
    print("Grade Point: 6")
    print("Remark: Pass")

elif(Marks<50):
    print("Grade Point: 0")
    print("Remark: Fail")