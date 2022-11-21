# E-Mail Slicer

# First Enter the number of E-Mails you want to provide then Enter E-Mails it will slice the gmail the separate the username and domain

RED = "\033[31m"
WHITE = "\033[m"
number = int(input("Enter no. of E-Mails you want to provide: "))
domaincontainer = []
usernamecontainer = []
for i in range(1, number+1):
    User_In = str(input("Enter {} E-Mail: ".format(i)))
    if "@" not in User_In:
        print(RED, "Neglecting this E-Mail, Enter Valid E-Mail !", WHITE)
        continue
    pos = User_In.find("@")
    usernamecontainer.append(User_In[:pos])
    domaincontainer.append(User_In[pos+1:])


print("Usernames after Slicing: ")
for i in range(1, len(usernamecontainer)+1):
    print("Username {}:".format(i), usernamecontainer[i-1])

print()
print("Domains after Slicing: ")
for i in range(1, len(domaincontainer)+1):
    print("Domains {}:".format(i), domaincontainer[i-1].upper())
