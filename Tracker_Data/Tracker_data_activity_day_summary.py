import pandas as pd
import os

file_path = '/Users/marcgruner/Downloads/samsunghealth_nevzad.nuhiu_202103172116/jsons/com.samsung.shealth.activity.day_summary'

df_activity_day_summary = pd.DataFame()

for sub_dir in os.listdir(file_path):
    print(sub_dir)
    if sub_dir == '.DS_Store': continue
    for filename in os.listdir(file_path+'/'+sub_dir):
        print(filename)
        temp_df = pd.read_json(filename)
        df_activity_day_summary.append(temp_df)

print(df_activity_day_summary)