# Project 11

# Random Number Status Checker Between given Range

import random


def is_prime(value):
    if value == 1 or value == 0 or value < 0:
        return "neither"
    for i in range(2, int(value/2)+1):
        if value % i == 0:
            return "composite"
    return "prime"


Start = int(input("Enter Starting Number: "))
Stop = int(input("Enter Ending Number: "))

if Start > Stop:
    print("Enter a valid range")
    exit()

value = random.randint(Start, Stop)
print("Selected Number is", value)


if value >= 0:
    print(value, "is a positive number")
else:
    print(value, "is a negative number")

if value % 2 == 0:
    print(value, "is an even number")
else:
    print(value, "is an odd number")

if is_prime(value) == "prime":
    print(value, "is a prime Number")
elif is_prime(value) == "composite":
    print(value, "is a composite Number")
else:
    print(value, "is neither prime nor composite")
