from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html')

@app.route('/leaderboard', methods=['POST', 'GET'])
def leaderboard():
    return render_template('leaderboard.html')

@app.route('/challenges', methods=['POST', 'GET'])
def recommendations():
    return render_template('challenges.html')

@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()


