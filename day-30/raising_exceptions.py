height = float(input('Height: '))
weight = float(input('Weight: '))

if height > 3:
    raise ValueError('Human height cannot be grater than 3 meters.')

bmi = weight / height ** 2

print(bmi)