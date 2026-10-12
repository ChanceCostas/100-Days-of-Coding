import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
desplay = []
for _ in range(len(chosen_word)):
    desplay += "_"
print(desplay)

oh_noo = False


while not oh_noo:
    guess = input("Guess a letter: ").lower()

    # TODO-2: Check the guess and update the display list at the right positions
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            desplay[position] = letter

    print(desplay)


    if "_" not in desplay:
        oh_noo = True
        print("You win!")