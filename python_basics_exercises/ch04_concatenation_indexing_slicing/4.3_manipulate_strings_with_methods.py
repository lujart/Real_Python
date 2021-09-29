#4.3 - Manipulate Strings with Methods
#Review Exercises

#Exercise 1 - Write a program that converts the following strings to lowercase. Print each lower-case string on a separate line.

string_1 = "Animals"
string_2 = "Badger"
string_3 = "Honey Bee"
string_4 = "Honey Badger"

print(string_1.lower())
print(string_2.lower())
print(string_3.lower())
print(string_4.lower())

#Exercise 2 - Repeat exercise 1, but convert each string to uppercase instead of lower case. 

print(string_1.upper())
print(string_2.upper())
print(string_3.upper())
print(string_4.upper())

#Exercise 3 - Write a program that removes whitespace from the following strings, then print out the strings with the whitespace removed:

string1 = "    Filet Mignon"
string2 = "Brisket    "
string3 = "      Cheeseburger     "

print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())

#Exercise 4 - Write a program that prints out the result of .startswith("be") on each of the following strings:

string1_1 = "Becomes"
string2_1 = "becomes"
string3_1 = "BEAR"
string4_1 = "   bEautiful"

print(string1_1.startswith("be"))
print(string2_1.startswith("be"))
print(string3_1.startswith("be"))
print(string4_1.startswith("be"))

#Exercise 5 - Using the same four strings in exercise 4, write a program that uses string methods to alter each string so that .startswith("be")
#returns True for all of them. 

print(string1_1.lower().startswith("be"))
print(string2_1.startswith("be"))
print(string3_1.lower().startswith("be"))
print(string4_1.lstrip().lower().startswith("be"))
