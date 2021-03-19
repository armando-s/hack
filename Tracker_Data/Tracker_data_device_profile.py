# import pandas as pd
import os

file_path = '/Users/marcgruner/Downloads/samsunghealth_nevzad.nuhiu_202103172116/jsons/com.samsung.health.device_profile'

df_device_profile = pd.DataFame()

for sub_dir in os.listdir(file_path):
    for filename in os.listdir(file_path+'/'+sub_dir):
        temp_df = pd.read_json(filename)
        df_device_profile.append(temp_df)