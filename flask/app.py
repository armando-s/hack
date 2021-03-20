from flask import Flask, render_template, redirect, request

app = Flask(__name__)

leaderboard_header = ('Rank','Icon','Name','Points')
leaderboard_data = (
    (1,'', 'Andri Turra', 173),
    (2,'', 'Armando', 165),
    (3,'', 'Marc', 147)
)

@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html')

@app.route('/leaderboard', methods=['POST', 'GET'])
def leaderboard():
    return render_template('leaderboard.html', leaderboard_header=leaderboard_header, leaderboard_data=leaderboard_data)

@app.route('/challenges', methods=['POST', 'GET'])
def recommendations():
    return render_template('challenges.html')

@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)


