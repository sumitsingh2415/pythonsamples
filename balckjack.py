import random
from replit import clear
from art import logo
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  next_card=random.choice(cards)
  return next_card

def calculate_score(user_list):
  if sum(user_list)==21 and len(user_list)==2:
    return 0
  
  if 11 in user_list and sum(user_list)>21:
    user_list.remove(11)
    user_list.append(1)

  return sum(user_list)


def compare(user_score, computer_score):
  if user_score==computer_score:
    return 'Draw'
  elif computer_score == 0:
    return ' Computer Wins, He has B;ackjack'
  elif user_score==0:
    return 'You Win'
  elif user_score>21:
    return 'You went over'
  elif user_score>computer_score:
    return 'You win'
  else:
    return 'Computer Wins'

def blackjack():
  print(logo)
  user_cards = []
  computer_cards = []
  game_over= False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not game_over:
    user_score= calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)

    print(f" User cards: {user_cards} and user_score: {user_score}")
    print(f" Computer first card {computer_cards[0]}")

    if user_score==0 or computer_score==0 or user_score>21:
      game_over=True
    else:
      should_continue = input("Enter 'y' to draw another card or 'n' to end the game: ")
      if should_continue=='y':
        user_cards.append(deal_card())
      else:
        game_over=True
      
  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand {user_cards} and score {user_score}")
  print(f"Computer final hand {computer_cards} and score {computer_score}")

  print(compare(user_score, computer_score))

  another_game=input("Enter 'yes' to restart  the game: ")
  if another_game=='yes':
    clear()
    blackjack()

blackjack()