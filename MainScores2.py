from flask import Flask, render_template
import Utils
import os

app = Flask(__name__)
    # read score from score file and return html


@app.route('/')
def scorehtml():
    filename = os.environ['SCORES_FILE_NAME']
    if os.path.exists(filename) and (os.path.getsize(filename) != 0):
    #if os.path.exists("Scores.txt"):
        print(5)
        text_file = open(filename, "r")
        result = int(text_file.read())
        return render_template('score.html', value=result)
        text_file.close()

    else:
    # file error
        return render_template('error.html')


def score_server():
    if __name__ == "__main__":
        app.run()

score_server()

