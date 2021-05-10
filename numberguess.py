#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
from replit import clear



def number_guessing_game():
  clear()
  print(logo)

  print("Welcome to the number guessing game!\nI am thinking of a number between 1 and 100\n")
  guess_remaining=0
  my_number=random.randrange(1,101)
  difficulty=input("Chose a difficulty, Type 'easy' or 'hard': ").lower()


  if difficulty=='easy':
    guess_remaining=10
  elif difficulty=='hard':
    guess_remaining=5
  else:
    print("Enter a valid input")

  number=0
  flag=True
  while guess_remaining>0 and number!=my_number:
    print(f"you have {guess_remaining} attempts remaining to guess the number:")
    number=int(input("Make a guess!"))

    if number>my_number:
      print('Too high!')
      guess_remaining-=1
    elif number<my_number:
      print('Too low')
      guess_remaining-=1
    else:
      flag=False
      print(f'Wohoo!! you have guessed it right, the number was {my_number}')
  if flag:
    print(f'You have exhausted your guesses!, the correct number was {my_number}')   

  play_again = input("Type 'yes' to play again: ")
  if play_again=='yes':
    number_guessing_game()


number_guessing_game()

