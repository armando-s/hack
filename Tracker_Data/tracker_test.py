import pandas as pd
import plotly.express as px

df = pd.read_csv('/Users/marcgruner/Desktop/Helsana_Hack/samsunghealth_nevzad.nuhiu_202103172116/test_com.samsung.shealth.step_daily_trend.202103172116.csv',sep=';')
df = df.drop( ['binning_data','update_time', 'create_time', 'source_pkg_name', 'deviceuuid','pkg_name', 'datauuid'],axis=1)
df = df[df['source_type']==-2]
df['day_time'] = pd.to_datetime(df['day_time'], unit='ms')
df['day_time'] = df['day_time'].dt.strftime('%Y-%m-%d %H')
df = df.sort_values('day_time')
print(df)
print(df.columns)
print(df.describe())

fig = px.bar(y=df['count'], x=df['day_time'])
fig.show()

