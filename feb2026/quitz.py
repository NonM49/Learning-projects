print("*** QUITS ***")
questions = {"How many leg a dog have?"       : "A.1, B.2, C.3, D.4",
             "How many teefth an adult have?" : "A.16, B.32, C.34, D.40",
             "What is a tomato?"              : "A.fruit, B.vetgetable",
             "what is the biggest animal?"    : "A.whale, B.elephent, C.hippo, D.human",
             }

answers = ["D", "B", "A", "A"]
score = 0 
index = 0
valid_choice =("A", "B", "C", "D")

for question in questions:
    print("\n" + question)
    print(questions.get(question) + "\n")
    while True:
        user_ans = input("Choose a correct choice (A/B/C/D): ").strip().upper()
        if user_ans in valid_choice:
            break
        else:
            print("Invalid Input")

    if user_ans == answers[index]:
        print("Correct answer!")
        score += 1
    else:
        print("Wrong answer!")

    index +=1

print(f"\nYour score : {score}/{len(answers)}")