# from Live import load_game, welcome
import sys
from CurrencyRouletteGameClass import CurrencyRollette
from GuessGameClass import GuessGame
from MemoryGameClass import MemoryGame


def welcome(name):
    print(f'Hello {name} and welcome to the World of Games (WoG) \nHere you can find many cool games to play. ')


def select_game():
    select = input('Please choose a game to play: \n'
                   '1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n'
                   '2. Guess Game - guess a number and see if you chose like the computer\n'
                   '3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n')
    if select.isdigit():
        select = int(select)
    else:
        print('You entered Illegal value , you will EXIT')
        sys.exit()
    return select


print(welcome("Michal"))
select1 = select_game()
if select1 == 1:
    a = MemoryGame()
    a.play()
elif select1 == 2:
    b = GuessGame()
    b.play()
elif select1 == 3:
    c = CurrencyRollette()
    c.play()
else:
    print('You entered Illegal game # value (should be 1-3 , you will EXIT')
    sys.exit()
