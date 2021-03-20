# import pandas as pd
import os

file_path = '/Users/marcgruner/Downloads/samsunghealth_nevzad.nuhiu_202103172116/jsons/com.samsung.shealth.sleep'

# df_sleep = pd.DataFame()

for sub_dir in os.listdir(file_path):
    print(sub_dir)
    if sub_dir == '.DS_Store': continue
    for filename in os.listdir(file_path+'/'+sub_dir):
        print(filename)
        # temp_df = pd.read_json(filename)
        # df_sleep.append(temp_df)