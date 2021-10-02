#Section 4.5 - Challenge: Pick apart your user's input.

# Write a program that prompts the user for input with the string "Tell me your password: ".
#The program should then determine the first letter of the user's input, convert that letter
#to upper case, and display it back. 

user_password = input("Tell me your password: ")
print("The first letter you entered was: " + user_password[0])

#Note: For now it's ok if the program crashes when the user enters nothing as input - that is, when
#the user types ENTER instead of typing something. We will deal with this situation in an upcoming
#chapter."
