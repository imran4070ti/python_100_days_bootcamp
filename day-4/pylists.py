dists = ['Rangpur', 'Panchagrah', 'Dinajpur', 'Kurigram', 'Nilphamari', 'Thakurgaon', 'Gaibandha']
print(dists[0])
print(dists[-1])

dists.append('Lalmonirhat')

print(dists)

dists.extend(['Bogura', 'Natore'])

print(dists)

dists.append(['Rajshahi', 'Dhaka'])

print(dists)
print(dists[-1])
print(type(dists[-1]))
