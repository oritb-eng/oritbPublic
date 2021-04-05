import random
import os
from time import sleep
import sys
from LiveClass import GenGame


class MemoryGame(GenGame):

    def generate_sequence(self, dif):
        num_list = []
        for num in range(dif):
            num_list.append(random.randint(1, 101))
        print(num_list)
        sleep(1)
        print("\n" * 100)
        #os.system('cls' if os.name == 'nt' else 'clear')
        return num_list

    def get_list_from_user(self , dif):
        num_list2 = []
        for num in range(dif):
            tmp = input("please enter number between 1 to 100")
            if tmp.isdigit():
                num = int(tmp)
                if 0 < num < 101:
                    num_list2.append(num)
                else:
                    print('You entered Illegal value , you will EXIT')
                    sys.exit()
            else:
                print('You entered Illegal value , you will EXIT')
                sys.exit()


        print(f'your numbers are {num_list2}')
        return num_list2

    def is_list_equal(self, src_list, user_list, dif):
        tmp_list = []
        tmp_list = list(set(src_list).intersection(user_list))
        print(tmp_list)
        print("you remembered ", len(tmp_list), 'numbers\n')
        if len(tmp_list) == dif:
            return True
        else:
            return False

    def play(self):
        dif = GenGame.load_game(self)
        list1 = self.generate_sequence(dif)
        list2 = self.get_list_from_user(dif)
        result = self.is_list_equal(list1, list2, dif)
        if result:
            print("Well Done you remembered all the numbers !!!")
        else:
            print('You did not remember all the numbers , Try again ')

