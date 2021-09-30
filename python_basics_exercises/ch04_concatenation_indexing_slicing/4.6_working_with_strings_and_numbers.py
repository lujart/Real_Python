#Section 4.6 - Working with Strings and Numbers
#Review Exercises

#Exercise 1 - Create a string containing an integer, then convert that string into
#an actual integer object using int(). Test that your new object is a number by multiplying
#it by another number and the result.

my_string_1 = "5"
my_integer = int(my_string_1)
product_1 = my_integer * 5
print(product)

#The result should be the number 25.

#Exercise 2 - Repeat the previous exercise, but use a floating-point number and float().

my_string_2 = "6"
my_float = float(my_string_2)
product_2 = my_float * 5.0
print(product_2)

#The result should be the decimal number 30.0

#Exercise 3 - Create a string object and an integer object, then display them side by side
#with a single print statement using str().

my_string_3 = "Red"
my_integer_3 = 5
print(my_string_3 + " " + str(my_integer_3))

#Exercise 4 - Write a program that uses input() twice to get two numbers from the user,
#multiplies the numbers together, and displays the result.

first_number = input("Please input the first number: ")
second_number = input("Please input the second number: ")

result = int(first_number) * int(second_number)

print("The product of " + str(first_number) + " and " str(second_number) + " is " + float(result) + ".") 
