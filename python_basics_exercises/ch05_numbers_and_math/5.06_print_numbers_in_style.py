# Section 5.6 - Print numbers in Style
# Review Exercises

# When using f-strings, the curly braces support a simple formatting language that can be used to alter the
# appearance of the value in the final formatting string. 

# For example, to format the value of a decimal number n to two decimal places, replace the contents of the
# curly braces in the f-string with {n:.2f}

# The colon (:) after the variable n indicates that everything after it is part of the formatting specification.
# In the previous example, the formatting specification is .2f.
# The .2 in .2f rounds the number to two decimal places, and the f tells Python to display n as a fixed-point
# number. This means that the number is diplayed with exactly two decimal places, even if the original number
# has fewer decimal places. 
# When you format a number as fixed point, it's always displayed with the precise number of decimal places
# that are specified.

# Also, commas can be inserted to group the integer part of large numbers by the thousands using: {n:,}

# To round to some number of decimal places and also group by thousands use: {n:,.2f}

# Another useful option is %, which is used to display percentages. The % option multiplies a number by 100 and
# displays it in fixed-point format, followed by a percentage sign.
# The % option should always go at the end of your formatting specification, and cannot be mixed with the f option. 
# Therefore, if ratio = 0.9, then {ratio:.1%} is 90.0%, {ratio:.2%} is 90.00%, and so on...

# Exercise 1 - Print the result of the calculation 3 ** .125 as a fixed-point number with three decimal places. 

result = 3 ** 0.125
print(f"The result is {result:.3f}")

# Exercise 2 - Print the number 150000 as currency with the thousands grouped with commas. Currency should be displayed
# with two decimal places.

number = 150000
print(f"{number:,.2f}")

# Exercise 3 - Print the result of 2 / 10 as a percentage with no decimal places. The output should look like 20%.

division = 2 / 10
print(f"{division:.0%}")

