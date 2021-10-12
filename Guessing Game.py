#Alex Evans
#Computer Programming 11
#September 15th, 2021
#Assignment 4 - Guessing Game

import random
d = 0
a = 0
b = 0
g = 2
topic_list = ["What is your favourite subject in school?", "What is your least favourite sport?", "What is your favourite colour?", "Who is your least favourite politician?", "What is your favourite pet?", "What is your favourite aquatic animal?", "What is your least favourite deep-sea animal?", "What is your favourite country?"]
print("This is a two-player guessing game.")
print("Player 1 will be asked a question, and will type an answer.")
print("Player 2 will then have to guess the answer Player 1 typed in.")
print("If Player 2 is correct, they will recieve 1 point.")
print("If they are incorrect, Player 1 will recieve 1 point.")
print("Then the turns will switch. Highest score after 5 rounds wins!")
print("Type 'Start' when you are both ready.")
start_response = input()
start_response = start_response.lower().strip(" ,./<>?;':[]{}`~1234567890!@#$%^&*()_+-=|")
if start_response == ("start"):
    d = 1
else:
    print("Error. Please restart the game.")
if d == 1:
    print("Good luck to all!")
    print("Player 1 may answer.")
    print(random.choice(topic_list))
    answerA_response = input()
    answerA_response = answerA_response.lower().strip(" ,./<>?;':[]{}`~1234567890!@#$%^&*()_+-=|")
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("Player 2, try and guess what Player 1 said!")
    answerB_response = input()
    answerB_response.lower().strip(" ,./<>?;':[]{}`~1234567890!@#$%^&*()_+-=|")
    if answerB_response == answerA_response:
        b = b + 1
        print("Congratulations, " + answerB_response + " was the right answer!")
        print("Player 2 now has 1 point!")
        print("Scores are as follows:")
    else:
        for i in range(g):
            g = g - 1
            print("Sorry, " + str(g + 1) + " guesses remaining")
            answerB_response = input()
            answerB_response = answerB_response.lower().strip(" ,./<>?;':[]{}`~1234567890!@#$%^&*()_+-=|")
            if answerB_response == answerA_response:
                b = b + 1
                print("Congratulations, " + answerB_response + " was the correct answer!")
                break
            if g == 0:
                print("Sorry, the correct answer was " + answerA_response + ". Better luck next time!")
                a = a + 1
                print("Scores are as follows:")
    print("Player 1 - " + str(a))
    print("Player 2 - " + str(b))
    print("Next round beginning...")
    g = 2
    print("Player 2 may answer")
    print(random.choice(topic_list))
    answerA_response = input()
    answerA_response = answerA_response.lower().strip(" ,./<>?;':[]{}`~1234567890!@#$%^&*()_+-=|")
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("Player 1, try and guess what Player 2 said!")
    answerB_response = input()
    answerB_response.lower().strip(" ,./<>?;':[]{}`~1234567890!@#$%^&*()_+-=|")
    if answerB_response == answerA_response:
        a = a + 1
        print("Congratulations, " + answerB_response + " was the right answer!")
        print("Player 1 now has " + str(a) + " points")
        print("Scores are as follows:")
    else:
        for i in range(g):
            g = g - 1
            print("Sorry, " + str(g + 1) + " guesses remaining")
            answerB_response = input()
            answerB_response = answerB_response.lower().strip(" ,./<>?;':[]{}`~1234567890!@#$%^&*()_+-=|")
            if answerB_response == answerA_response:
                a = a + 1
                print("Congratulations, " + answerB_response + " was the correct answer!")
                break
            if g == 0:
                print("Sorry, the correct answer was " + answerA_response + ". Better luck next time!")
                b = b + 1
                print("Scores are as follows:")
    g = 2
    print("Player 1 - " + str(a))
    print("Player 2 - " + str(b))
    print("Next round beginning...")
    print("Player 1 may answer")
    print(random.choice(topic_list))
    answerA_response = input()
    answerA_response = answerA_response.lower().strip(" ,./<>?;':[]{}`~1234567890!@#$%^&*()_+-=|")
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("Player 2, try and guess what Player 1 said!")
    answerB_response = input()
    answerB_response.lower().strip(" ,./<>?;':[]{}`~1234567890!@#$%^&*()_+-=|")
    if answerB_response == answerA_response:
        b = b + 1
        print("Congratulations, " + answerB_response + " was the right answer!")
        print("Player 2 now has " + str(b) + " points")
        print("Scores are as follows:")
    else:
        for i in range(g):
            g = g - 1
            print("Sorry, " + str(g + 1) + " guesses remaining")
            answerB_response = input()
            answerB_response = answerB_response.lower().strip(" ,./<>?;':[]{}`~1234567890!@#$%^&*()_+-=|")
            if answerB_response == answerA_response:
                b = b + 1
                print("Congratulations, " + answerB_response + " was the correct answer!")
                break
            if g == 0:
                print("Sorry, the correct answer was " + answerA_response + ". Better luck next time!")
                a = a + 1
                print("Scores are as follows:")
    g = 2
    print("Player 1 - " + str(a))
    print("Player 2 - " + str(b))
    print("Next round beginning...")
    print("Player 2 may answer")
    print(random.choice(topic_list))
    answerA_response = input()
    answerA_response = answerA_response.lower().strip(" ,./<>?;':[]{}`~1234567890!@#$%^&*()_+-=|")
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("Player 1, try and guess what Player 2 said!")
    answerB_response = input()
    answerB_response.lower().strip(" ,./<>?;':[]{}`~1234567890!@#$%^&*()_+-=|")
    if answerB_response == answerA_response:
        a = a + 1
        print("Congratulations, " + answerB_response + " was the right answer!")
        print("Player 2 now has " + str(b) + " points")
        print("Scores are as follows:")
    else:
        for i in range(g):
            g = g - 1
            print("Sorry, " + str(g + 1) + " guesses remaining")
            answerB_response = input()
            answerB_response = answerB_response.lower().strip(" ,./<>?;':[]{}`~1234567890!@#$%^&*()_+-=|")
            if answerB_response == answerA_response:
                b = b + 1
                print("Congratulations, " + answerB_response + " was the correct answer!")
                break
            if g == 0:
                print("Sorry, the correct answer was " + answerA_response + ". Better luck next time!")
                b = b + 1
                print("Scores are as follows:")
    g = 2
    print("Player 1 - " + str(a))
    print("Player 2 - " + str(b))
    print("Next round beginning...")
    print("Player 1 may answer")
    print(random.choice(topic_list))
    answerA_response = input()
    answerA_response = answerA_response.lower().strip(" ,./<>?;':[]{}`~1234567890!@#$%^&*()_+-=|")
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("Player 2, try and guess what Player 1 said!")
    answerB_response = input()
    answerB_response.lower().strip(" ,./<>?;':[]{}`~1234567890!@#$%^&*()_+-=|")
    if answerB_response == answerA_response:
        b = b + 1
        print("Congratulations, " + answerB_response + " was the right answer!")
        print("Player 2 now has " + str(b) + " points")
        print("Scores are as follows:")
    else:
        for i in range(g):
            g = g - 1
            print("Sorry, " + str(g + 1) + " guesses remaining")
            answerB_response = input()
            answerB_response = answerB_response.lower().strip(" ,./<>?;':[]{}`~1234567890!@#$%^&*()_+-=|")
            if answerB_response == answerA_response:
                b = b + 1
                print("Congratulations, " + answerB_response + " was the correct answer!")
                break
            if g == 0:
                print("Sorry, the correct answer was " + answerA_response + ". Better luck next time!")
                a = a + 1
    if a == 5 or b == 5:
        print("Game over!")
        if a == 5:
            print("Player 1 wins!")
        if b == 5:
            print("Player 2 wins!")
        print("Sweeeeeeep!")
        print("Final score:")
        print("Player 1 - " + str(a))
        print("Player 2 - " + str(b))
        print("Thanks for playing!!!")
    else:
        print("Game over!")
        if a > b:
            print("Player 1 wins!")
        if b > a:
            print("Player 2 wins!")
        print("Final score:")
        print("Player 1 - " + str(a))
        print("Player 2 - " + str(b))
        print("Thanks for playing!!!")
