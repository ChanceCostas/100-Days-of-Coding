import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
print("Welcome to blackjack game, let's get started all right!")

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

player_card1 = random.choice(cards)
player_card2 = random.choice(cards)
total_player_cards = player_card1 + player_card2

dealer_card1 = random.choice(cards)
dealer_card2 = random.choice(cards)
total_dealer_cards = dealer_card1 + dealer_card2

print(f"You have {player_card1} and {player_card2}")
print(f"The dealer has {dealer_card1} and ?????")
print(f"Your total is: {total_player_cards}")

while total_player_cards < 21:
    go_again = input("Do you want to pick more cards again? (y/n): ").lower()

    if go_again == "y":
        new_card = random.choice(cards)
        total_player_cards += new_card
        print(f"You drew a {new_card}! Your new total is {total_player_cards}")
    elif go_again == "n":
        break
    else:
        print("Please type 'y' or 'n'.")

print("\n--- FINAL RESULTS ---")
print(f"Dealer's cards: {dealer_card1} and {dealer_card2} (Total: {total_dealer_cards})")
print(f"Your total: {total_player_cards}")

if total_player_cards > 21:
    print("You went over 21! You lose! ")
elif total_dealer_cards > 21:
    print("Dealer went over 21! You win! ")
elif total_player_cards > total_dealer_cards:
    print("You have more than the dealer! You win! ")
elif total_player_cards < total_dealer_cards:
    print("Dealer has more than you. You lose!")
else:
    print("It's a draw!")

































































































































































print("good game also if you like the gane you can build more if you use python cya")