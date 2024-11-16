Names=["Utkarsh","Chirag","Aakrisht","Aryan"]
Roll_no=[5,22,20,3]
Marks=[95,91,93,90]

Record=zip(Names,Roll_no,Marks)
X=list(Record)
print(X)

sorted_students = sorted(X, key=lambda x: x[2])
print(sorted_students)