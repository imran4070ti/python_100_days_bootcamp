student_dict = {
    "student":['A', 'B', 'C'],
    "id" : [1, 2, 3]
}


for keys, values in student_dict.items():
    print(keys, values)


import pandas as pd


student_df = pd.DataFrame(student_dict)

# print(student_df)


for idx, row in student_df.iterrows():
    print(row['id'])