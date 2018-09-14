import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

timetable = { 
            'day' : ['mon','tues','wed','thurs','fri', 'sat'],
            'No_classes' : [4, 5, 6, 3, 3, 2],
            'free_periods' : [3, 4, 5, 6, 1, 2]}

df = pd.DataFrame(timetable)

#to print the table
print(df)

#to print top except last value
print(df.head())

#to print last except top value
print(df.tail())

#to print using index
print(df.tail(2))

#to give title to index
#df.set_index('Day', inplace=True)

#to access particular rows or columns
print(df['day'])

#to access multiple keys
print(df[['day','No_classes']])

#to convert to a list
print(df['day'].tolist())

#you cannot convert 2d list into adn array ,without import numpy as np
import numpy as np
print(np.array(df[['day','No_classes']]))

#passing array to pandas
df2 = pd.DataFrame(np.array(df[['day','No_classes']]))
print(df2)



