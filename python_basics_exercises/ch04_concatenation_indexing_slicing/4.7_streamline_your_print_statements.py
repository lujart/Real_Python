#Section 4.7 - Streamline your print statements
#Review Exercises

#So far I have used 'string interpolations' to insert some varables into specific locations in a string.
#To achieve the same effect, form now on I will be using 'formatted string literals'; more commonly known as 'f-strings'.

#There are two important things to consider:
#1) The string literal starts with the letter f before the opening quotation mark.
#2) Variable names must be surrounded by curly braces {}, replacing their corresponding values without using str().

#Exercise 1 - Create a float object named weight with the value 0.2, and create a string object named animal with
#the value "newt". Then use these objects to print the following string using only string concatenation:
#"0.2 kg is the weight of the newt".

weight = 0.2
animal = "newt"

print(str(weight) + " kg is the weight of the " + animal + ".")

#Exercise 2 - Display the same string by using .format() and empty {} placeholders.

#Note: f-strings are available only in Python version 3.6 and above. In earlier versions of Python, 
#formatted string literals could be achieved by using .format() a the end of the sentence to be 
#printed. e.g.: "{} has {} heads {} and {} arms".format(name, heads, arms) 
#where "name", "heads" and "arms" are previously defined variables. 

print("{} kg is the weight of the {}.".format(weight, animal))

#Exercise 3 - Display the same string using an f-string.

print(f"{weight} kg is the weight of the {animal}.")
