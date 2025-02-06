def numProperDivisors(num):
    properDivisors = []
    for x in range (1,num // 2 + 1):
        if num % x == 0:
            properDivisors.append(x)
    return properDivisors

number = int(input('Enter number : '))


properDivisors = numProperDivisors(number) 

if sum(properDivisors) == number:
    print(f"{number} is a perfect number")
else:
    print(f"{number} is not a perfect number")

