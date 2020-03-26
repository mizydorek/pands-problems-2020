# Maciej Izydorek
# read in a number from input, substract 10% and print out
# throw an error if the input is less then 0

sub = 0.90 

number = float(input('input a number: '))

if ( number < 0 ):
    raise ValueError("input should be greater than 0 ({})".format(number))

ans = number * sub 
print("{} minus 10% is {}".format(number,ans))

