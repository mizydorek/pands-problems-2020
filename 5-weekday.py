# Maciej Izydorek
# Checks if wheteher or not today is a weekday

import datetime
# Get today's date
now = datetime.datetime.now()
# check if wheteher or not today is a weekday knowing that 
# Monday equals to 0 and Sunday equals 6
if now.weekday() < 5:
    print('Yes, unfortunately today is a weekday.')
else:
    print('It is the weekend, yay!')