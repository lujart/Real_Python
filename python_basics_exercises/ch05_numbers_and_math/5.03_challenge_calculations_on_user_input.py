# Section 5.3 - Challenge: Perform Calculations on User Input.

# Write a program that received two numbers from the user and siplays the first number raised
# to the power of the second number.

base = input("Enter a base: ")
exponent = input("Enter an exponent: ")

# Remember: input() returns a string, so I'll need to convert the user's input into numbers
# to do arithmetic.

result = float(base) * float(exponent)

print(f"{base} to the power of {exponent} = {result}")
