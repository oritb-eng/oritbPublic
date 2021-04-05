import os
import Utils


def add_score(difficulty=1):
    # read score file and add value
    points = difficulty * 3 + 5
    filename = os.environ['SCORES_FILE_NAME']
    #text_file = open(filename, "r+")
    if os.path.exists(filename) and (os.path.getsize(filename) != 0):
        text_file = open(filename, "r+")
        value = int(text_file.read())
        result = value+points
        text_file.seek(0)
        text_file.write(str(result))
        print(result)
        text_file.close()
    else:
        text_file = open(filename, "w+")
        text_file.write(str(points))
        value = text_file.read()
        text_file.close()

add_score()
