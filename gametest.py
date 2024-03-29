import random

try:
    l = ["rock", "scissor", "paper"]

    while True:
        ucount = 0
        ccount = 0

        uc = int(input('''
        Loading the game...
        Press 1 to Enter
        Press 2 to Exit
        '''
        ))

        if uc == 1:
            print("Thank you for starting the game")
            for a in range(1, 6):
                userinput = int(input('''
                Press 1 for rock
                Press 2 for scissor
                Press 3 for paper
                '''))

                if userinput == 1:
                    uchoice = "rock"
                elif userinput == 2:
                    uchoice = "scissor"
                elif userinput == 3:
                    uchoice = "paper"
                else:
                    print("Please check your choice, it should be 1, 2, or 3")
                    continue  # Move the continue statement here to skip the rest of the loop
                cinput = random.choice(l)

                if cinput == uchoice:
                    print(f"Game is draw.your choice is {uchoice}, computer's choice is {cinput}")
                elif (uchoice == "rock" and cinput == "scissor") or (uchoice == "scissor" and cinput == "paper") or (uchoice == "paper" and cinput == "rock"):
                    print(f"Your choice is {uchoice}, computer's choice is {cinput}")
                    ucount += 1
                    print(f"You won, total points are {ucount}, {ccount}")
                else:
                    print(f"Your choice is {uchoice}, Computer's choice is {cinput}")
                    ccount += 1
                    print(f"You lost, total points are {ucount}, {ccount}")

            # Display the final result after 5 rounds
            print(f"\nFinal Scores - Your score: {ucount}, Computer's score: {ccount}")

            # Determine the final winner after 5 rounds
            if ucount > ccount:
                print("Congratulations! You are the final winner.")
            elif ucount < ccount:
                print("Computer is the final winner.")
            else:
                print("The game is a draw.")

        elif uc == 2:
            print("Exiting the Game")
            break
        else:
            print("Entered value is incorrect")

except ValueError:
    print("Entered value is not correct")
