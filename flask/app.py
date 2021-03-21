from flask import Flask, render_template, redirect, request, Markup
from operator import itemgetter
import pandas as pd
import plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import json
from datetime import timedelta

app = Flask(__name__)




@app.route('/', methods=['POST', 'GET'])
def home():
    fig = make_subplots(
        rows=2, cols=2,
        specs=[[{"type": "xy"}, {"type": "xy"}],
               [{"type": "xy"}, {"type": "xy"}]],
        subplot_titles=("Steps", "Burned Calories", "Heartrate", "Sleep"),
        horizontal_spacing=0.1,
        vertical_spacing=0.1,
    )


    df_steps = pd.read_csv('static/test_com.samsung.shealth.step_daily_trend.202103172116.csv',sep=';')
    df_steps = df_steps.drop(['binning_data', 'update_time', 'create_time', 'source_pkg_name', 'deviceuuid', 'pkg_name', 'datauuid'], axis=1)
    df_steps = df_steps[df_steps['source_type'] == -2]
    df_steps['day_time'] = pd.to_datetime(df_steps['day_time'], unit='ms')
    df_steps['day_time'] = df_steps['day_time'].dt.strftime('%Y-%m-%d %H')
    df_steps['day_time'] = pd.to_datetime(df_steps['day_time']) + timedelta(days=3)
    df_steps = df_steps.sort_values('day_time')
    df_steps = df_steps.tail(30)
    df_steps['average'] = df_steps['count'].mean()
    fig.add_trace(go.Bar(y=df_steps['count'], x=df_steps['day_time'], showlegend=False, marker_color=['#E55187']*len(df_steps)), row=1, col=1)

    df_hr = pd.read_csv('static/hr.csv', sep=';')
    df_hr = df_hr.sort_values('TS')
    df_hr['TS'] = pd.to_datetime(df_hr['TS']) + timedelta(days=6)
    df_hr = df_hr[df_hr['TS'] >= '2021-03-20 00:00:00']
    fig.add_trace(go.Scatter(x=df_hr['TS'], y=df_hr['com.samsung.health.heart_rate.heart_rate'], showlegend=False, marker_color='#E55187'), row=2, col=1)

    df_cal = pd.read_csv('static/cal.csv', sep=';')
    df_cal = df_cal.rename(columns={'com.samsung.shealth.calories_burned.active_time': 'active_time',
                                    'com.samsung.shealth.calories_burned.rest_calorie': 'Resting Calories',
                                    'com.samsung.shealth.calories_burned.active_calorie': 'Active Calories',
                                    'com.samsung.shealth.calories_burned.day_time': 'TS'}, inplace=False)
    df_cal = df_cal.drop(['Unnamed: 4', 'Unnamed: 5'], axis=1)
    df_cal['TS'] = pd.to_datetime(df_cal['TS'], unit='ms')
    df_cal['TS'] = df_cal['TS'].dt.strftime('%Y-%m-%d')
    df_cal['TS'] = pd.to_datetime(df_cal['TS']) + timedelta(days=3)
    df_cal = df_cal.sort_values('TS')
    df_cal = df_cal.tail(30)
    fig.add_trace(go.Bar(x=df_cal['TS'], y=df_cal['Resting Calories'],offsetgroup=0, name='Resting Calories', marker_color='#61AEDE'), row=1, col=2)
    fig.add_trace(go.Bar(x=df_cal['TS'], y=df_cal['Active Calories'], offsetgroup=0, name='Active Calories', marker_color='#990842',base=df_cal['Resting Calories']), row=1, col=2)



    df_sleep = pd.read_csv('static/sleep_stage.csv', sep=';')
    df_sleep = df_sleep.convert_dtypes()
    df_sleep['start_time'] = pd.to_datetime(df_sleep['start_time'])
    df_sleep['end_time'] = pd.to_datetime(df_sleep['end_time'])
    df_sleep['start_time'] = df_sleep['start_time'].dt.strftime('%Y-%m-%d %H:%M')
    df_sleep['end_time'] = df_sleep['end_time'].dt.strftime('%Y-%m-%d %H:%M')
    df_sleep['start_time'] = pd.to_datetime(df_sleep['start_time']) + timedelta(days=6)
    df_sleep['end_time'] = pd.to_datetime(df_sleep['end_time']) + timedelta(days=6)
    df_sleep = df_sleep[df_sleep['start_time'] >= '2021-03-19 20:00:00']
    df_sleep.loc[df_sleep['stage'] == 40001, 'stage_'] = 'awake'
    df_sleep.loc[df_sleep['stage'] == 40002, 'stage_'] = 'light'
    df_sleep.loc[df_sleep['stage'] == 40003, 'stage_'] = 'deep'
    df_sleep.loc[df_sleep['stage'] == 40004, 'stage_'] = 'REM'
    df_sleep = df_sleep.sort_values('start_time')
    fig.add_trace(go.Scatter(x=df_sleep['start_time'], y=df_sleep['stage'], showlegend=False, marker_color='#E55187'), row=2, col=2)

    fig.update_yaxes(autorange='reversed',tickmode='array',tickvals=[40001,40002,40003,40004],ticktext=['awake', 'light', 'deep', 'REM'], row=2,col=2)
    fig.update_layout(height=600)
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_layout(margin=dict(l=10, r=10, t=30, b=10))
    fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=0.95, xanchor="right", x=1, bgcolor="rgba(0, 0, 0, 0)", ))

    plot_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


    return render_template('home.html', plot_json=plot_json)


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


if __name__ == '__main__':
    app.run()