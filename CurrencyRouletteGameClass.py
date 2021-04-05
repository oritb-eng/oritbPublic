import urllib.request
import json
import random
import time
import sys
from LiveClass import GenGame


class CurrencyRollette():
    def __init__(self):
        self.money = random.randint(1, 101)

    def get_money_interval(self, difficulty):
        json_url = "https://api.exchangeratesapi.io/latest?base=USD"
        response = urllib.request.urlopen(json_url)
        data = json.loads(response.read().decode(response.info().get_param('charset') or 'utf-8'))
        currency = data['rates']['ILS']
        interval = (self.money*currency - (5 - difficulty), self.money*currency +(5 - difficulty))
        #print(f'money in ILS : {self.money*currency}', f'interval is : {interval}')
        return self.money*currency, interval

    def get_guess_from_user(self):
        guess = input(f'Enter ILS for the {self.money} in UDS')
        if guess.isdigit():
            guess = int(guess)
        else:
            print('You entered Illegal value , you will EXIT')
            sys.exit()
        return guess

    def play(self):
        dif = GenGame.load_game(self)
        curr, interval1 = self.get_money_interval(dif)
        user_guess = self.get_guess_from_user()
        interval1 = sorted(interval1)
        bottom = interval1[0]
        top = interval1[1]
        if bottom < user_guess < top:
            print("Your answer is correct ")
            print(f'money in ILS : {curr}', f'interval is : {bottom , top}')
            return True
        else:
            print('Incorrect answer , try again')
            print(f'money in ILS : {curr}', f'interval is : {bottom , top}')
            return False



