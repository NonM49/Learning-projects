import random
print("Password Generator!!")
leg = int(input("Length: "))
sym = input("Enter any letter or symbols you want to include: ")
syms = list(sym)

print("Password : ", end="")

for i in range(leg):
    print(random.choice(syms), end="")