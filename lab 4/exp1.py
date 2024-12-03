s=input("Enter a sentence:")

words=s.split()
count=0

for word in words:
    rev_word=word[::-1]
    if(rev_word==word):
        count=count+1

print(f"The number of palindrome words in a given sentence is {count} ")