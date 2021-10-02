# Section 4.8 - Find a String in a String
# Review Exercises

# A string within a string is commonly referred to as a substring. 
# For this, use .find() tacking it to the end of a variable or a string literal
# with the string you want to find typed between the parentheses.

#Important things to remember:
#1) This method returns the index of the first occurance of the string you pass to it.
#2) If the desired substring is not found, it will return -1 instead.
#3) This matching is done exactly, character by characterm and is case sensitive.
#4) If a substring appears more than once in a string, then .find() returns the index of
# only the first appearance, starting from the beginning of the string. 
#5) This method only accepts a string as its input. If you want to find an integer in a string,
# then you need to pass the integer to .find() as a string. Otherwise, Python raises a TypeError. 

# Also, this section features the method .replace():
# This is used when you have to find all ocurrances of a particular substring and replace them
# with a different string. 
# Just like with .find(), you tack .replace() onto the end of a variable or string literal.
# In this case, though, you need to put two strings inside the parentheses in .replace() and
# separate them with a comma. The first string is the substring to find, and the second string is
# string with which to replace each ocurrance of the substring.

#Exercise 1 - In one line of code, display the result of trying to .find() the substring "a" in the
# "a" in the string "AAA". The result should be -1.

my_string = "AAA"
print(my_string.find("a"))

#Exercise 2 - Replace every occurance of the character "s" with "x" in the string "Somebody said something to Samatha".

second_string = "Somebody said something to Samantha"
print(second_string.replace("s", "x"))

#Exercise 3 - Write a program that accepts user input with input() and displays the result of trying to .find()
# a particular letter in that input. 

favourite_colour = input("What is you favourite colour?: ")
letter_g = favourite_colour.find("g")
if letter_g < 0:
  print("The letter 'g' is not present in that word.")
else:
  print(f"In that word, the first letter 'g' found corresponds to index {letter_g}.")
    
# By the time I created this repository I already new how to work with if/else statements, so I couln't resist
# making this program a bit more interesting. 
