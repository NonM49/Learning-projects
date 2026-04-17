import random

print("*** NUMBER GUESSING GAME ***")
print("- Guess a number between 1 to 100")

while True:

    answer = random.randint(1, 100)
    tries = 0

    while True:
        try:
            guess = int(input("Enter a number: "))
            tries += 1

            if guess == answer:
                print("Congreat! You guessed the number")
                print(f"You guessed {tries} times")
                break
            elif guess < answer:
                print("* Too low! *")
            elif guess > answer:
                print("* Too high! *")
        except ValueError:
            print("Please enter a whole number")
    
    while True:
        play_again = input("Play again? (y/n): ").lower()
        if play_again == "y":
            break
        elif play_again == "n":
            quit()
        else:
            print("Invalid")



        


