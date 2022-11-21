
# Program to find prime or composite in a given range

starting, ending = input("Enter Starting and ending number of range: ").split()
a = int(starting)
b = int(ending)

for i in range(a, b+1):
    if i == 1 or i == 0:
        print(i, "is neither prime nor composite")
        continue

    for j in range(2, int(i/2)+1):
        if i % j == 0:
            print(i, "is a composite number")
            break
    else:

        print(i, "is a prime number")
