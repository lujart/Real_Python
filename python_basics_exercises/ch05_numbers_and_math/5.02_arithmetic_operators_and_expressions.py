# 5.2 - Arithmetic Operators and Expressions

# This section offers a review on how to do basic arithmetic. There are no Review Exercises as such.
# So just as a brief reminder of the contents of this section, here are few operations.

# Addition:

sum1 = 1 + 2
print(sum1)
# result is 3 as an integer

sum2 = 1.0 + 2
print(sum2)
# result is 3.0 an a float

# Same rules apply to Substraction:

subs1 = 1 - 1
print(subs1)
# result is be 0

subs2 = 5.0 - 3
print(subs2)
# result is 2.0

# Multiplication:

mult1 = 3 * 3
print(mult1)
# result is 9

mult2 = 2 * 8.0
print(mult2)
# result is 16.0

# Division:

div1 = 9 / 3
print(div1)
# result is 3

div2 = 5.0 / 2
print(div2)
# result is 2.5

# Unlike addition, subtraction, and multiplications, division with the / operator always returns
# a float. To make sure I will get an integer after dividing two numbers, int() must be used to
# convert the result.

div3 = int(9 / 3)
print(div3)
# result is 3

# It is important to keep in mind that int() discards any fractional part of the number:

div4 = int(5.0 / 2)
print(div4)
# result is 2

# Integer Division:
# Python provides a second division operator called the integer division operator (//), also know as
# the floor division operator:

int_div1 = 9 // 3
print(int_div)
# result is 3

int_div2 = 5.0 // 2
print(int_div2)
# result is 2.0

# When trying to divide a number by zero, Python will return a 'ZeroDivisionError'.

# Exponents:

exp1 = 2 ** 2
print(exp1)
# result is 4

# Exponents don;t have to be integers. They can also be floats:

exp2 = 3 ** 1.5
print(exp2)
# result is 5.1961152422706632

exp3 = 9 ** 0.5
print(exp3)
# result is 3.0

# numbers can also be raised to negative powers:

exp4 = 2 ** -1
print(exp4)
# result is 0.5

# The Modulus Operator
# The % operator, of the modulus, returns the remainder of dividing the left operand by the right operand:

mod1 = 5 % 3
print(mod1)
# result is 2

# One of the most common uses of % is to determine whether one number is divisible by another. For example,
# a number n is even if and only if n % 2 is 0.

# Things get trickier when the % operator is used with negative numbers:

mod2 = 5 % -3
print(mod2)
# result is -1

# This result is the product of a well-defined behaviour in Python. To calculate the remainder r of dividing
# a number y, Python uses the equation: r = x - (y * (x // y))
