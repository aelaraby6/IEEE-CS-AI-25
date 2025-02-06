import sys

number = int(input("Enter the number: "))

if number < 0:
    sys.exit(0)

sumDigits = 0

while number > 0:
    sumDigits += number % 10
    number //= 10

print(f"Sum of digits is: {sumDigits}")
