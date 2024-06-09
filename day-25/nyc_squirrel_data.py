import pandas as pd

df = pd.read_csv('day-25/nyc_squirrel_data.csv')
# print(df.columns)
# print(df[df['Primary Fur Color'] == 'Gray']['Primary Fur Color'].count())

data_dict = {
    'Fur Color' : ['Gray', 'Red', 'Black'],
    'Count' : [df[df['Primary Fur Color'] == 'Gray']['Primary Fur Color'].count(), df[df['Primary Fur Color'] == 'Cinnamon']['Primary Fur Color'].count(),  df[df['Primary Fur Color'] == 'Black']['Primary Fur Color'].count()]
}

color_df = pd.DataFrame(data_dict)
print(color_df)

color_df.to_csv('day-25/squirrel_count.csv')