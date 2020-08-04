
"""
	1. Asks user to enter number "x"
	2. asks user to enter number "y"
	3. print out number "x", raised to power "y"
	4. Prints out log (base2) of "x"
"""
import math

x = float(input('Enter number x:'))
y = float(input('Enter number y:'))
print('x**y = ',x**y)
print('log(x) = ', math.log(x,2))