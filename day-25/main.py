import pandas as pd


# Dataframe -> Whole table
# Series -> A column


# data = pd.read_csv('day-25/weather_data.csv')

# data_dict = data.to_dict()

# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)

# print(data['temp'].mean())


# print(data[data.day == 'Monday'])

# print(data[data.day == 'Monday'].temp + 273)


data_dict = {
    'name':['A', 'B', 'C'],
    'id' : [1, 2, 3]
}

df = pd.DataFrame(data_dict)
print(df)
print(type(df))