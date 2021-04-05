import os

#try:
#    env_var = input('Please enter environment variable name for Score file name:\n')
#except:
#env_var = 'Scores.txt'

os.environ['SCORES_FILE_NAME'] = 'Scores.txt'
print('SCORES_FILE_NAME=', os.environ['SCORES_FILE_NAME'], 'environment variable has been set.')
os.environ['BAD_RETURN_CODE'] = '0'
print('BAD_RETURN_CODE=', os.environ['BAD_RETURN_CODE'], 'environment variable has been set.')


def screen_cleaner():
    print("\n" * 100)
    #os.system('cls' if os.name == 'nt' else 'clear')