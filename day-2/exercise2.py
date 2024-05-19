# BMI calculator

height = input('Enter your height in meter: ')
weight = input('Enter your weight in KG: ')

height = float(height)
weight = float(weight)

bmi =round( weight / float(height)**2)
# bmi = weight // float(height)**2 #flooring

print('Your BMI is: ' + str(bmi))