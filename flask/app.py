from flask import Flask, render_template, redirect, request, Markup
from operator import itemgetter

app = Flask(__name__)




@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html')


@app.route('/leaderboard', methods=['POST', 'GET'])
def leaderboard():
    leaderboard_header = ('Rank', '', 'Name', 'Points')
    leaderboard_data = [['alexis78', 152], ['gvang', 62], ['millerchase', 30], ['katiejones', 20], ['qware', 44], ['lmorrison', 85], ['amy05', 36], ['yjohnson', 11], ['cfisher', 159], ['barnesjill', 3], ['robin15', 41], ['shelbyzamora', 20], ['xbailey', 129], ['mariostephens', 1], ['joanna33', 156], ['andersonhayley', 91], ['michelle04', 133], ['bryanjones', 113], ['landerson', 164], ['wellsdaniel', 149], ['hendersonkelly', 79], ['silvagarrett', 94], ['jacob80', 169], ['kelliblake', 148], ['pcox', 8], ['stricklandbrian', 68], ['kathleen21', 110], ['mendezchristopher', 77], ['stephen91', 86], ['smitchell', 55], ['jamiesharp', 39], ['monica01', 39], ['sandersrandy', 147], ['karenhill', 73], ['bowendebbie', 165], ['estephens', 167], ['normanmichael', 134], ['egreen', 79], ['ramirezmartin', 9], ['meghanlee', 160], ['lindsey37', 121], ['stevenmcclain', 158], ['angela08', 120], ['stephanieaguirre', 9], ['richard56', 120], ['kimberly04', 110], ['edwardlopez', 77], ['mark64', 133], ['nicholas04', 92], ['maxdorsey', 90]]

    leaderboard_data = sorted(leaderboard_data, key=itemgetter(1), reverse=True)
    for rank in range(len(leaderboard_data)):
        leaderboard_data[rank].insert(0,rank+1)
        if rank == 0:
            leaderboard_data[rank].insert(1,Markup('<img src="/static/badge_gold.png" class="leaderboard_badge">'))
        elif rank == 1:
            leaderboard_data[rank].insert(1, Markup('<img src="/static/badge_silver.png" class="leaderboard_badge">'))
        elif rank == 2:
            leaderboard_data[rank].insert(1, Markup('<img src="/static/badge_bronze.png" class="leaderboard_badge">'))
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