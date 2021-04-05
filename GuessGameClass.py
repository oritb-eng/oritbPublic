from LiveClass import GenGame
import random
import sys


class GuessGame():

    def generate_number(self, dif):
        secret_number = random.randint(1, dif)
        return secret_number

    def get_guess_from_user(self, dif):
        num = input(f'Please enter number between 1 to {dif}')
        if num.isdigit():
            num = int(num)
        else:
            print('You entered Illegal value , you will EXIT')
            sys.exit()
        if 0 < num < (dif + 1):
            return num
        else:
            print('You entered Illegal value , you will EXIT')
            sys.exit()


    def compare_results(self , secret_number ,guess_num ):
        result = False
        if secret_number == guess_num:
            result = True
        return result


    def play(self):
        dif = GenGame.load_game(self)
        secret_num = self.generate_number(dif)
        guess_num = self.get_guess_from_user(dif)
        result = self.compare_results(secret_num, guess_num)
        print(f'The correct number {secret_num}', f'your guess is :{guess_num}')
        if result:
            print("Very good ! You succeeded to guess the number !! ")
        else:
            print('You did not guess the correct number , Try again ')



