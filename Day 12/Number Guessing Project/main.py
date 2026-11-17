import random



numbers = list(range(1, 101))
random_number = random.choice(numbers)

takes = input("Welcome to the guessing game! Would you like to play easy mode or hard mode? For easy mode type 'easy', for hard mode type 'hard': ")
realtakes = takes.lower()

if realtakes == "easy":
    guesses = 10
else:
    guesses = 5

while guesses > 0:
    print(f"\nYou have {guesses} guesses remaining.")
    player_guess = int(input("Guess a number between 1 and 100: "))

    if player_guess == random_number:
        print("You guessed the number! You win!")
        break
    elif player_guess > random_number:
        print("Too high.")
    else:
        print("Too low.")

    guesses -= 1

if guesses == 0:
    print(f"\nYou lose! The number was {random_number}.")























































































