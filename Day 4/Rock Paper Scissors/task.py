import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the Rock Paper Scissors game!")


user_input = input("Type rock, paper, or scissors: ").lower()


if user_input == "rock":
    ted = rock
elif user_input == "paper":
    ted = paper
elif user_input == "scissors":
    ted = scissors
else:
    ted = None


if ted is None:
    print("Please put a correct input!")
else:
    # Print the user's choice
    print(ted)


    ramdom = random.randint(1, 3)


    print("Bot chose:")
    if ramdom == 1:
        print(rock)
        bot_choice = "rock"
    elif ramdom == 2:
        print(paper)
        bot_choice = "paper"
    else:
        print(scissors)
        bot_choice = "scissors"


    if user_input == bot_choice:
        print("It's a tie!")
    elif (user_input == "rock" and bot_choice == "scissors") or \
            (user_input == "paper" and bot_choice == "rock") or \
            (user_input == "scissors" and bot_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

    print("\nHave a great day!")

























































































































































































