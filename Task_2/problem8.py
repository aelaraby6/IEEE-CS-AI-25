import random

tries = 5 
num = random.randint(1,100)
counter = 0

while counter < tries:
    guess = int(input())
    counter+=16
    if guess < num:
            print("Try a higher number.")
    elif guess > num:
            print("Try a lower number.")
    else:
        print(f"Congratulations! You guessed the number in {counter} tries!")
        break

