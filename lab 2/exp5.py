import math
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))

d=(b*b)-(4*a*c)

if(d==0):
    R1=R2=-b/2*a
    print("Roots are: ",R1," and ",R2)

if(d>0):
    R1=(-b+math.sqrt(d))/(2*a)
    R2=(-b-math.sqrt(d))/(2*a)
    print("Roots are: ",R1," and ",R2)

if(d<0):
    real_part=-b/(2*a)
    imaginary_part=math.sqrt(-d)/(2*a)
    
    print("Roots are: ")
    print((real_part)/" + i "(imaginary_part))