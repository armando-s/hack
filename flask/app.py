from flask import Flask, render_template, redirect, request, Markup
from operator import itemgetter
import pandas as pd
import plotly
import plotly.express as px
import json

app = Flask(__name__)




@app.route('/', methods=['POST', 'GET'])
def home():
    df_steps = pd.read_csv('static/test_com.samsung.shealth.step_daily_trend.202103172116.csv',sep=';')
    df_steps = df_steps.drop(['binning_data', 'update_time', 'create_time', 'source_pkg_name', 'deviceuuid', 'pkg_name', 'datauuid'], axis=1)
    df_steps = df_steps[df_steps['source_type'] == -2]
    df_steps['day_time'] = pd.to_datetime(df_steps['day_time'], unit='ms')
    df_steps['day_time'] = df_steps['day_time'].dt.strftime('%Y-%m-%d %H')
    df_steps = df_steps.sort_values('day_time')
    df_steps = df_steps.tail(30)
    df_steps['average'] = df_steps['count'].mean()
    fig = px.line(y=df_steps['average'], x=df_steps['day_time'], color_discrete_sequence=['#E55187']*len(df_steps))
    fig.add_bar(x=df_steps['day_time'], y=df_steps['count'], marker=dict(color="#990842"))
    fig.update_layout({'plot_bgcolor':'rgba(0, 0, 0, 0)'})
    fig.update_layout(showlegend=False)
    fig.update_xaxes(title=None)
    fig.update_yaxes(title=None)
    plot_steps_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('home.html', plot_steps_json=plot_steps_json,
                           plot_sleep_json=plot_steps_json,
                           plot_calo_json=plot_steps_json,
                           plot_hr_json=plot_steps_json)


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