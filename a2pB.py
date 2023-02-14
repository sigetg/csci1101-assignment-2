# Write a program that solves the quadratic equation of the form ax2+bx+c = 0.
# You must prompt the user for the values of a, b, and c, which could be any
# numbers.  You can assume the user will not enter non-numeric values.  To
# solve for x, you have to calculate the roots of the equation.  To do that,
# you have to first calculate the discriminant d: d=b^2-4ac.  Then follow this
# logic (see assignment for formula details):
#
# If the discriminant is negative, then the roots are imaginary.  Print a
# message informing the user of this and stop the program.
#
# If the discriminant is exactly zero, then there is a single root.
#
# If the discriminant is positive, then there are two roots.
#
# Your input and output messages must conform to the following examples (the
# comment lines won’t be in your program output, of course, they are there to
# help explain the output): 
#
# Example with imaginary roots
# Enter a: 1
# Enter b: 2
# Enter c: 3
# Roots = imaginary
#
# Example with one root
# Enter a: 1
# Enter b: 4
# Enter c: 4
# Root = -2.00
#
# Example with two roots
# Enter a: 1
# Enter b: 3
# Enter c: 2
# Roots = -1.00, -2.00
#
# Note the order of outputs, capitalization of messages, spacing, etc.

import math
a = float(input("Enter value for a: ")) 
b = float(input("Enter value for b: "))
c = float(input("Enter value for c: "))

d = b**2 - 4*a*c

if d<0:
    print("The roots are imaginary")
else:
    if d>0:
        print(f"Roots = {(-b + math.sqrt(d)) / 2*a}, {(-b - math.sqrt(d)) / 2*a}")
    else:
        print(f"Root = {-b / 2*a}")
 


