
import random

name = input("What is your name? : ")
print("Good luck ! ", name)

words = ["apple", "tiger", "chair", "bread", "river",
         "planet", "forest", "window", "guitar", "rocket",
         "marble", "shadow", "lantern", "puzzle"]


while True:

    print("* Welcome to Guess the Word game *")
    word = random.choice(words)
    hint = ["_"] * len(word)
    num_guesses = 0
    guesses = set()

    while True:

        print()
        print(" ".join(hint))
        guess = input("guess a character: ").lower()
        

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid")
            continue

        if guess in guesses:
            print(f"{guess} is already guessed.")
            continue

        guesses.add(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    hint[i] = guess
            num_guesses += 1
        else:
            num_guesses += 1
            continue

        if "_" not in hint:
            print(" ".join(hint))
            print(" You Win! ")
            print(f"You guess {num_guesses} times.")
            break

    play_again = input("Play again? (y/n) : ").lower()
    if play_again != "y":
        print("Thanks for playing!")
        break

    




    











