from flask import Flask, render_template, redirect, request, Markup
from operator import itemgetter

app = Flask(__name__)




@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html')


@app.route('/leaderboard', methods=['POST', 'GET'])
def leaderboard():
    leaderboard_header = ('Rank', '', 'Name', 'Points')
    leaderboard_data = [
        ['Andri Turra', 173],
        ['Armando Schmid', 165],
        ['Marc Gruener', 147],
        ['Peter Griffin', 2],
        ['Homer Simpson', 5],
        ['Clark Kent', 9001],
    ]

    leaderboard_data = sorted(leaderboard_data, key=itemgetter(1), reverse=True)
    for rank in range(len(leaderboard_data)):
        leaderboard_data[rank].insert(0,rank+1)
        if rank == 0:
            leaderboard_data[rank].insert(1,Markup('<img src="/static/League5.png">'))
        elif rank == 1:
            leaderboard_data[rank].insert(1, Markup('<img src="/static/League5.png">'))
        elif rank == 2:
            leaderboard_data[rank].insert(1, Markup('<img src="/static/League5.png">'))
        else:
            leaderboard_data[rank].insert(1,'')


    return render_template('leaderboard.html', leaderboard_header=leaderboard_header, leaderboard_data=leaderboard_data)


@app.route('/challenges', methods=['POST', 'GET'])
def recommendations():
    return render_template('challenges.html')


@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)