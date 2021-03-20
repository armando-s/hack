import pandas as pd
import os

file_path = '/Users/marcgruner/Downloads/samsunghealth_nevzad.nuhiu_202103172116/jsons/com.samsung.health.user_profile'

# df_user_profile = pd.DataFame()

for sub_dir in os.listdir(file_path):
    for filename in os.listdir(file_path+'/'+sub_dir):
        print(filename)
        # temp_df = pd.read_json(filename)
        # df_user_profile.append(temp_df)