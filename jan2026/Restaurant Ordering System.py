

menu = {"pizza": 3.00,
        "hamberger": 5.00,
        "chiken wings": 7.00,
        "coke": 2.00,
        "sprite": 2.00,
        "lemonade": 1.50}

cart = []
total = 0

print("-----MENU-----")
for key, value in menu.items():
    print(f"{key:^13}: ${value:.2f}")
print("--------------")

while True:
    food = input("select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is None:
        print("Invalid")
    else:
        cart.append(food)
        print(f"added {food}..")

print("--------- YOUR ORDER ---------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")