
class bank:

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be a positive amount.\n")
            return
        self.balance += amount
        print(f"deposit : +${amount}")
        print(f"You balance : ${self.balance}\n")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw must be a positive amount.\n")
            return
        if amount > self.balance:
            print("Not enough money.\n")
            return
        self.balance -= amount
        print(f"withdraw : -${amount}")
        print(f"You balance : ${self.balance}\n")

    def check_balance(self):
        print(f"You have ${self.balance}\n")

def ask_amount():
    while True:
        try:
            return float(input("Amount : "))
        except ValueError:
            print("Invalid number.")
            continue
        

print("BANK SIMULATER")

account1 = bank("Non")
account2 = bank("Noch")
accounts = [account1, account2]

while True:
    ask_acc = input(f"Which account? [Non, Noch] : ").capitalize()
    for acc in accounts:
        if ask_acc == acc.owner:
            current_acc = acc
            break
    else:
        print("Account not found.")
        continue
    break


while True:
    print(f"\nAccount : {current_acc.owner}")

    print(
          "1.Balance",
          "2.Deposit",
          "3.Withdraw",
          "4.Quit", sep = "\n"
          )
    
    try:
        choice = int(input("What would you like to do? : "))
    except ValueError:
        print("Enter a number 1 - 4.")
        continue

    if choice == 1:
        current_acc.check_balance()

    elif choice == 2:
        amount = ask_amount()
        current_acc.deposit(amount)

    elif choice == 3:
        amount = ask_amount()
        current_acc.withdraw(amount)

    elif choice == 4:
        print("Quiting...")
        break

    else:
        print("Invalid choice.")