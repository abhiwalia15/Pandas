import pandas as pd

dict = {'name': ['abhi','lovee','ishu','mouli'],
		'age': [19,21,14,13],
		'location':['blr','vlr','ptk','ptk'],
		}
		
df = pd.DataFrame(dict)
print(df)

print(df.tail(3))

df.index.name = 'No.'
print(df)

df.columns.name = 'order'
print(df)

print(df['age'])

print(df[['age','location']])

df.to_html('personal_details.html') 
df.to_html('personal_details.html', header = False)

df.rename(columns = {'name':'humra_name' , 'age':'umaar'}, inplace=True)
print(df)


