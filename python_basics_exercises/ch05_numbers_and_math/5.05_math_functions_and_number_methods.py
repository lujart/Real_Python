# Section 5.5 - Math Functions and Number Methods
# Review Exercises

# Python has a few built-in functions that can be used to work with numbers:

# 1. round(), for rounding numbers to some number of decimal places.
# 2. abs(), for getting the absolute value of a number.
# 3. pow(), for raising a number to somo power. 

# There is also a method that can be used with floating-point numbers to check whether
# they have an integer value.

# Floating-point numbers have an .is_integer() method that returns True if the number is
# integral -meaning it has no fractional part- and otherwise returns false.

# Exercise 1 - Write a program that asks the user to input a number and then displays that
# number rounded to two decimal places.

user_input = input("Enter a number: ")
print(f"{user_input} rounded to 2 decimal places is {round(float(user_input), 2)}")

# Exercise 2 - Write a program that asks the user to input a number and then displays the 
# absolute value of that number. 

user_input_2 = input("Enter a number: ")
print(f"The absolute value of {user_input_2} is {abs(float(user_input_2))}")

# Exercise 3 - Write a program that asks the user to input two numbers by using input() twice,
# then displays whether the difference between those two numbers is an integer. 

user_input3 = input("Enter a number: ")
another_number = input("Enter another number: ")

difference = float(user_input3) - float(another_number)

print(f"The difference between {user_input3} and {another_number} is an integer? " + difference.is_integer() + "!")



