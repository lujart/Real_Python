# Section 4.1 - What is a String?
# Review Exercises

# Strings are one of the fundamental data types bult into Python. 
# We say that strings are a fundamental data type because they can't be broken
# down into smaller values of a different type. Not all data types are fundamental.
# In Chapter 9, I will learn about compound data types, also called data structures.

# The string data type has a special abbreviated name in Python: str()

# Python has a built-in len() function that can be used to determine the length
# of a string. 

# For multi-line strings, there are two methods:

# The first one is to break the string across multiple lines and put a backlash (\)
# at the end of all but the last line. To be PEP8 compliant, the total length of the
# line, including the backslashes, must be seventy-nine characters or fewer.

# The second method is using triple quotes (""" or ''') as delimeters. Triple-quoted strings
# preserve whitespace, including newlines. 

# Exercise 1 - Print a string that uses double quotation marks inside the string.

string_1 = 'Darth Vader said, "I, am your father..." '
print(string_1)

# Exercise 2 - Print a string that uses an apostrophe inside the string

string_2 = "He said that after cutting off Luke's right hand."
print(string_2)

# Exercise 3 - Print a string that spans multiple lines with whitespace preserved. 

string_3 = '''This scene takes place in deep inside the Cloud
City, located in the gas-giant planet called Bespin. 
                          This appears in my favourite Star
           Wars film "Episode V - The Empire Strikes       Back".'''

# Exercise 4 - Print a string that is coded on multiple lines but gets printed on
# a single line.

string_4 = "Hi,\
how\
are\
you?"


