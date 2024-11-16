import math
a =  int(input("Enter a : "))
b =  int(input("Enter b : "))
c =  int(input("Enter c : "))

perimeter = a+b+c
print("Perimeter of triangle : ", perimeter)
s = perimeter/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle : ", area)

A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
C = math.acos((a**2 + b**2 - c**2) / (2 * a * b))

A = math.degrees(A)
B = math.degrees(B)
C = math.degrees(C)

print("Angle A:",A)
print("Angle B:",B)
print("Angle C",C)