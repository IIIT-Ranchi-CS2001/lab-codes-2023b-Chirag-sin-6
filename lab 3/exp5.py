s = input("Enter string: ")

for i in s:
    if  not s.isalnum():
        print(f"{s} is not alphanumeric")
        break
else:
        print(f"{s} is alphanumeric")