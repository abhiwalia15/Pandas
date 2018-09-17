import pandas as pd

#to read the csv data
df = pd.read_csv('NSE-HAL.csv')

#set the index to day
df.index.name = 'DAY'
print(df.head())

#save the result to a csv_file.
df.to_csv('HINDUSTAN_Aeronautics Limited.csv')

#save the file in html format
df.to_html('HINDUSTAN_Aeronautics Limited.html')

#if you dont want to print the header.
df.to_csv('HINDUSTAN_Aeronautics Limited1.csv', header=False)

#how to rename the columns
df.rename(columns={'Close':'khtm'}, inplace=True)

