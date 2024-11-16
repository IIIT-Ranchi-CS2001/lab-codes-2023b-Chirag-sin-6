n=int(input("Enter a number:"))
m=n
sum=0
i=1
while(n>0):
    l=n%10
    n=n/10
    sum=sum+l
    i=i+1
print("Number is:",m)
print("Sum of digits:",int(sum))