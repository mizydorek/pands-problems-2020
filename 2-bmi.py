# Maciej Izydorek
# Progam that calculates BMI 

# two variables weight and height that hold user input and converts to float 
weight = float(input('Enter weight in kg: '))
height = float(input('Enter height in cm: '))

#formula that calculates bmi and round the result to two decimal points 
bmi = round( weight / ( height / 100 ) ** 2,2 )   
#print out output of bmi 
print('BMI is', bmi)