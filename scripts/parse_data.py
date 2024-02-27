import os
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

root_dir = './youtube-data'

# Create an empty dictionary to store dataframes
dfs = {}

encoded_password = quote_plus("postgres")
engine = create_engine(f'postgresql://postgres:{encoded_password}@localhost:15432/youtube_data')

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith('.csv') and filename != 'Totals.csv':
            df_name = f"{os.path.basename(dirpath)}_{os.path.splitext(filename)[0]}"
            df_name = df_name.replace(' ', '_').lower()
            df = pd.read_csv(os.path.join(dirpath, filename))
            dfs[df_name] = df

Total_Views_by_Day = pd.read_csv('./youtube-data/Cities/Totals.csv')
dfs['total_views_by_day'] = Total_Views_by_Day

for df_name, df in dfs.items():
    print(df_name)
    print(df.head())

for df_name, df in dfs.items():
    df.to_sql(df_name, engine, if_exists='replace')