# 4.9 Challenge: Turn your user into a L33t H4wor.

# Write a program that asks the user for some input with the following prompt:
# Enter some text:

# Use .replace() to convert the text entered by the user into 'leetspeak' by making the following changes
# to lowercase letters:

# The letter a becomes 4.
# The letter b becomes 8.
# The leeter e becomes 3. 
# The letter l becomes 1. 
# The letter o becomes 0.
# The letter s becomes 5.
# The letter t becomes 7.

# Your program should then display the result string as output. 

my_string = input("Enter some text: ")
my_string = my_string.lower().replace("a", "4")
my_string = my_string.replace("b", "8")
my_string = my_string.replace("e", "3")
my_string = my_string.replace("l", "1")
my_string = my_string.replace("o", "0")
my_string = my_string.replace("s", "5")
my_string = my_string.replace("t", "7")

print(my_string)
