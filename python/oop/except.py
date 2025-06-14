# import math
 
# number = -5
 
# print('Calculating the logarithm of', number)
# try:
#     print(math.log(number))
# except ValueError:
#     print('Unable to calculate logarithm of', number, 'because it is a negative number. Please provide another number.')
import math
x = 1
y = -2
 
try:
    value = x / y
    print(math.log(value))
except (ZeroDivisionError, ValueError) as e:
    print('Got an error:', e)