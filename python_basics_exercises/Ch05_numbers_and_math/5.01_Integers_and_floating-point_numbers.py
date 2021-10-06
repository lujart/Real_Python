# 5.1 Integers and Floating-Point Numbers
# Review Exercises

# Python has three built-in numeric data types: integers, floating-point numbers, and complex numbers.
# This section will be dedicated to integers and floating-point numbers.
# Complex numbers will be studied in section 5.7

# Exercise 1 - Write a progra, that creates two variables, num1 and num2. Both varables should be assigned
# the integer literal 25000000, onew written with underscores and one without. Print num1 and num2 on two
# separate lines. 

num1 = 25000000
num2 = 25_000_000

print(num1)
print(num2)

# Exercise 2 - Write a program that assignes the floating-point literal 175000.00 to the variable num using
# E-notation and then prints num in the interactive window. 

num = float(175e3)
print(num)

# Exercise 3 - Try to find the smallest exponent N for which 2e<N>, where <N> is replaced with your
# number, returns inf. 

small_number = 2e-400
