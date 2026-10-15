import random
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list
# TODO-3: - Import the logo and stages from hangman_art.py
from hangman_art import logo, stages

print(logo)

lives = 6

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
   
    print(f"****************************{lives}/6 LIVES LEFT****************************WHY U LOSE A LIVE TIMMY CAN LOSE NOOOO LIVES BUT TIMMY IS NOT A FAILURE YOU ARE A BADDDDD'")
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print(f"You've already guessed the letter '{guess}'. Try a different one!")
        continue

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter

            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(f"Word to guess: {display}")

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            # TODO 7: - Update the print statement below to give the user the correct word.
            print(f"***********************YOU LOSE**********************")
            print(f"The correct word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(stages[lives])









