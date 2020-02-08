# Maciej Izydorek
# Progam that calculates BMI 

weight = float(input('Enter weight in kg: '))
height = float(input('Enter height in cm: '))

bmi = round( weight / ( height / 100 ) ** 2,2 )   #formula that calculates bmi and round the result to two decimal points 
print('BMI is', bmi)