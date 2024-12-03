def fibonacci_series(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=' ')
        a, b = b, a + b 
        count += 1

n = int(input("Enter the number of terms: "))
if n <= 0:
    print("Please enter a positive integer")
else:
    print(f"The first {n} terms of the Fibonacci series are:")
    fibonacci_series(n)
