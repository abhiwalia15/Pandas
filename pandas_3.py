import pandas as pd

#to read the csv data
df = pd.read_csv('NSE-HAL.csv')

#set the index to day
df.index.name = 'DAY'
print(df.head())

#save the result to a csv_file.
df.to_csv('HINDUSTAN_Aeronautics Limited.csv')
