lst = input("Enter String").split(" ")

print([x.upper() for x in list(filter(lambda x : x.isalpha(), lst))])
print([int(x)**2 for x in list(filter(lambda x : x.isnumeric(), lst))])
print([x for x in list(filter(lambda x : x.isalnum(), lst))])