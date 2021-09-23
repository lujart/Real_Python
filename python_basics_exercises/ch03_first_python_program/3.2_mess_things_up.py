#3.2 - Mess Things Up
#Review Exercises

#Exercise 1 - Write a program that the editor won't run because it has a syntax error.

print("Hi)
      
#The problem here is that the absence of the double quotes at the end of the string. 
      
#Exercise 2 - Write a program that crashes only while it's running because it has a runtime error.
      
''' The following lines won't run properly,
even if the syntax error in the line above is corrected,
because of a run-time error'''
      
print(Hello)
      
#For this to work correctly the string should be enclosed by double or sinle quotes;
# as "Hello" or 'Hello'.
      
#Alternatively,  a variable called Hello does not exist.
#if so, this could have been written like this:

# my_string = "Hello"
# print(my_string)
      
