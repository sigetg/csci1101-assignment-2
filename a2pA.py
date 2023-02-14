# Write a program to calculate the standard deviation of 4 numbers.  Your
# program must prompt the user for 4 numbers (you can assume they will be
# numbers and not strings).  Note that the numbers need not be whole numbers.
# See the assignment for the full formula. Don’t try to calculate it all in one
# step!  Instead, do the following:
#
# 1. Calculate the mean (sum all the numbers, divide by how many numbers there are).
# 2. Calculate the difference between each number and the mean, and square it.
# 3. Add up each of the squared differences from above, then divide by N.
# 4. Finally, take the square root.
#  
# You must display the mean and standard deviation to three decimal places.
# Your input and output messages must conform to the following example:
#
# Enter the first number: 1
# Enter the second number: 2
# Enter the third number: 3
# Enter the fourth number: 4
# Mean = 2.500
# Standard Deviation = 1.118
#
# Note the order of inputs, capitalization of messages, spacing, etc. 

import math
number_1 = float(input("Enter the first number:"))
number_2 = float(input("Enter the second number:"))
number_3 = float(input("Enter the third number:"))
number_4 = float(input("Enter the fourth number:"))

mean = (number_1 + number_2 + number_3 + number_4) / 4

a = (number_1 - mean)**2
b = (number_2 - mean)**2
c = (number_3 - mean)**2
d = (number_4 - mean)**2

e = (a+b+c+d) / 4

standard_deviation = math.sqrt(e)

print(f"Mean: {mean:.3f}")
print(f"Standard Deviation: {standard_deviation:.3f}")
