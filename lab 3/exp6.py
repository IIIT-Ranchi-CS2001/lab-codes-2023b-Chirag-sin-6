def count_occurrences(string, char_to_find):
    count = 0
    for char in string:
        if char == char_to_find:
            count += 1
    return count


S = input("Enter a string: ")
character = input("Enter the character to find: ")
occurrences = count_occurrences(S, character)
print(f"The character '{character}' occurs {occurrences} times in the string.")
