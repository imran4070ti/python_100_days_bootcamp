# BMI calculator

height = input('Enter your height in meter: ')
weight = input('Enter your weight in KG: ')

height = float(height)
weight = float(weight)

bmi = weight / float(height)**2
# bmi = weight // float(height)**2 #flooring

print(f'Your BMI is: {bmi:.2f}')

if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<25:
    print('Normal weight')
elif bmi>=25 and bmi<30:
    print('Overweight')
elif bmi>=30 and bmi<35:
    print('Obese')
else:
    print('Clinically obese')

