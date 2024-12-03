employee_salaries = {}
n = int(input("Enter the number of employees (at least 5): "))

for _ in range(n):
    name = input("Enter employee name: ")
    salary = int(input(f"Enter salary for {name}: "))
    employee_salaries[name] = salary

employees = list(employee_salaries.items())

for i in range(len(employees)):
    for j in range(0, len(employees) - i - 1):
        if employees[j][1] < employees[j + 1][1]:
            employees[j], employees[j + 1] = employees[j + 1], employees[j]  

print("Employees sorted by salary (highest first):")
for rank, (name, salary) in enumerate(employees, start=1):
    print(f"{rank}. {name}: Rs. {salary}")
