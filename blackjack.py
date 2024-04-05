import random
import sys,subprocess


def deal_card():
    """ this function will tell us distribute random cards to players"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) != 2:
        return 0

    if 11 in cards and sum(cards) > 21:
          cards.remove(11)
          cards.append(1)
    return sum(cards)



def compare(user_score, computer_score):
    """ this function is used to compare the scores and return the result"""
    if user_score==computer_score:
      return "Draw"
    elif computer_score==0:
      return "lose, computer has a blackjack"
    elif user_score==0:
      return "Win with a blackjack"
    elif user_score>21:
      return "You went over, You lose"
    elif computer_score>21:
      return "Opponent went over, You Win"
    elif user_score>computer_score:
      return "Your win,Your score is closer to Blackjack,"
    else:
      return (f"yOU LOSE, opponents score is {computer_score} ")


def blackjack():
    """ this is the main games function 

    """
    print("""
    
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           

    """)
    user_cards = []
    computer_cards = []
    is_game_over=False
    for i in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())
    while is_game_over == False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards:{user_cards}  Your current score:{user_score}")
        print(f"Computer/Dealer's first card:{computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_hit = input("Type 'y' to get another card type 'n' to pass: ")
            if user_should_hit == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final_score: {user_score}")
    print(f"Computer's final hand:{computer_cards}, final score:{computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of black jack? type 'y' for YES and 'n' for NO: ") == "y":

    blackjack()
   


