import random

cards =['Ace of Hearts', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts',
    'Ace of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds',
    'Ace of Clubs', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs',
    'Ace of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades']
playerCards = []
houseCards = []
playerWins = []
houseWins = []
ties = []
playerChips = [20]

def blackjack():
    for i in range(2):
        random.shuffle(cards)
        playerCards = [cards.pop()]
        playerCards.append(cards.pop())
        houseCards = [cards.pop()]
        houseCards.append(cards.pop())
    
    bet = input("How many chips will you bet?\n>>")   
    print("Your hand is", playerCards[0], "and", playerCards[1])
    call = input("What would you like to do? \n>>1. Stay\n>>2. Hit\n>>").lower()
        
    if call == "1" or call == "stay":
        print("The House had", houseCards)
    elif call == "2" or call == "hit":    
        playerCards = [cards.pop()]
        playerCards.append(cards.pop())
        print("Your hand is", playerCards[0], "and", playerCards[1], "and", playerCards[2])

def blackjackIntro():
    print("Welcome to Blackjack!")
    rulesAsk = input("Would you like to learn how to play Blackjack?\n>>1. Yes\n>>2. No, I already know\n>>").lower()
    if rulesAsk == "1" or rulesAsk == "yes":
        print("In Blackjack, you start with 2 cards handed to you by the house. The goal of the game is to get as close to or at 21 without going over. All numbered cards are face value, with Jacks, Queens, and Kings all worth 10. Aces are specialty cards, as they count as 11, EXCEPT for if the value of all your cards added together goes above 21, in which case it counts as a value of one. When it's your turn, either Hit and get another card to increase your value or Stay to keep your value where it is. In this single-player Python Blackjack game, it's just you versus the house computer to see who can get a higher score. This game includes some more experienced features, such as splitting, but those you can look up on your own, as these are just the basics. Game on!\n")
        blackjack()
    elif rulesAsk == "2" or rulesAsk == "no" or rulesAsk == "no, i already know":
        print("Alright, experienced player. Game on!\n")
        blackjack()

# BEGINNING OF THE ACTUAL PROGRAM

play = input("Hello! Would you like to play Blackjack?\n>>1. Yes\n>>2. No\n>>").lower()

if play == "yes" or play == "1":
    blackjackIntro()
elif play == "no" or play == "2":
    quit()


#REMADE BLACKJACK DEF WITH while

def blackjack():
    global playerCards, houseCards, houseWins, playerWins  # Ensure you reference global variables here

    while True:
        print("Your hand is:")
        print(playerCards)
        print("The house has:")
        print(houseCards[0])  # Displaying only the house's first card

        call = input("What would you like to do?\n>>1. Stay\n>>2. Hit\n>>").lower()

        if call == "1" or call == "stay":
            print("The House had", houseCards)
            # Perform comparisons and determine the winner based on the rules of Blackjack
            # Ensure you adjust the condition based on the total value of cards
            # Implement logic to compare the total value of cards between player and house
            # Adjust the code here to compare total card values
            player_total = calculate_total(playerCards)
            house_total = calculate_total(houseCards)

            if house_total > player_total and house_total <= 21:
                print("House wins. The House had:")
                print(houseCards)
                houseWins += 1
            elif player_total < house_total or player_total > 21:
                print("You win. The house had:")
                print(houseCards)
                playerWins += 1
            else:
                print("It's a tie!")

            break  # Exit the while loop after determining the winner when the player stays

        elif call == "2" or call == "hit":
            playerCards.append(cards.pop())
            print("Your hand is:")
            print(playerCards)

            # Calculate the total value of playerCards and check if it exceeds 21
            player_total = calculate_total(playerCards)
            if player_total > 21:
                print("You busted!")
                break  # Exit the loop if the player busts (total > 21)

