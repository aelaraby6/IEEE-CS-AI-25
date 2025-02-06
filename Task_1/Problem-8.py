word = input('Enter the word : ')

if word == (word[::-1]):
    print(f"The word {word} is a palindrome.")
else:
    print(f"The word {word} is not a palindrome.")
