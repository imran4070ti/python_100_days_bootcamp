'''
{
    key1 : [List],
    key2 : {Dict}
}
'''



# Simple Dictionary with key-value pair
capitals = {
    'Bangladesh' : 'Dhaka',
    'India' : 'New Delhi',
    'Sri Lanka' : 'Colombo',
    'Pakisthan' : 'Islamabad'
}

# Nested dictionary
divisions = [
    {
        'name' : 'Rangpur',
        'dicts' : ['Rangpur', 'Panchagrah', 'Thakurgaon', 'Nilphamari', 'Lalmonirhat', 'Kurigram', 'Gaibandha', 'Dinajpur'],
        'total_districts' : 8
    },
    {
        'name' : 'Rangpur',
        'dicts' : ['Bogura', 'Natore', 'Naogaon', 'Rajshahi', 'Pabna', 'Sirajganj', 'Chapainababganj', 'Joypurhat'],
        'total_districts' : 8
    }
]


def add_new_division(name, districts, total_districts):
    new_division = {
        'name' : name,
        'districts' : districts,
        'total_districts' : total_districts
    }

    # new_division = {}
    # new_division['name'] = name
    # new_division['districts'] = districts
    # new_division['total_districts'] = total_districts

    divisions.append(new_division)


# for division in divisions:
#     name = division['name']
#     districts = division['dicts']
#     total_dicts = division['total_districts']
#     print(f'There are total {total_dicts} in {name} division. And they are: ')
#     for district in districts:
#         print(district)
#     print()


print(len(divisions))
add_new_division('Dhaka', ['Dhaka', 'Manikganj', 'Tangail', 'Gazipur'], 4)
print(len(divisions))
print(divisions)

    