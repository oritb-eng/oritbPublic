import sys
from abc import ABC, abstractmethod


class GenGame(ABC):
    def __init__(self):
        self.dif = 1

    @abstractmethod
    def play(self):
        pass

    def load_game(self):

        select2 = input('Please choose game difficulty from 1 to 5:\n')
        if select2.isdigit():
            self.dif = int(select2)
            if self.dif > 5 or self.dif < 1:
                print('You entered Illegal value , your difficulty will be set to 1')
                self.dif = 1
        else:
            print('You entered Illegal value , you will EXIT')
            sys.exit()
        return self.dif



