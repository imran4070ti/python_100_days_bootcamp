pydict = dict()
print(type(pydict))

pydict.update({
    'Imran':'1234567890',
    'Ruman':'0123456789'
})


for item in pydict.items():
    name = item[0]
    phone = item[1]
    print(f'Name: {name}\tPhone no: {phone}')

pydict.update({
    'Hasan' : '1357902468'
})

for item in pydict.items():
    name = item[0]
    phone = item[1]
    print(f'Name: {name}\tPhone no: {phone}')

hasan = pydict.get('Hasan')
print(hasan)
pydict.pop('Hasan')

for item in pydict.items():
    name = item[0]
    phone = item[1]
    print(f'Name: {name}\tPhone no: {phone}')

pydict['Hasan'] = '1357902468' # Instead of pydict.update()

for item in pydict.items():
    name = item[0]
    phone = item[1]
    print(f'Name: {name}\tPhone no: {phone}')

print(len(pydict))

# pydict.clear() # pydict={}

# print(len(pydict))

for item in pydict.items():
    print(type(item))


# for item in pydict: -> will return only the keys
# for item in pydict.items() -> will return (key, value) pairs as tuples