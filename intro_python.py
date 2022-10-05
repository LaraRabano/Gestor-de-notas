#######################################
## Printing and variables

age = 30 # This is how you declare a variable, think this like a box who saves information (data type)

# print(age)
# print(40)

age = 40

# print(age)

# this is a comment

# age, age123, age_123 -> Correct
# Use snake_case -> first_name
# Camelcase -> firstName, more common in languages like Javascript

# Variables that are constant (never change) usually are uppercase

HEIGHT = 1.72

# print(HEIGHT)

# Carefull to not give reserved names to variables
# for, if, else, elif, while, true, false...




#######################################
## Number (integers and float) Data Type

age = 35 # integer / int
PI = 3.1425 # Float

maths_operations = 1 + 3 * 4 / 2 - 2 # When we divide we always get a float
# print(maths_operations)

float_division = 12 / 3 # -> 4.0
integer_division = 12 // 3 # -> 4

type(float_division)
type(integer_division)

# print(type(float_division))
# print(type(integer_division))




#######################################
## Calculating the remainder of a division (How to get a remainder)

division = 12 // 5
# print(division)

division = 10 % 9
# print(division)



#######################################
## Strings (Another Data Type)

double_quote_string = "Hello, World!"
single_quote_string = 'Hello, World!'

# my_string = "Hello, World' -> Don't work

string_with_quotes = 'Hello it\'s me'
# print(string_with_quotes)

multiline = "Hello World! \nMy name is Lara."
# print(multiline)

multiline = """
Hello, World!

My name is Lara.
"""

# print(type(multiline))


#######################################
## String operations

name = "Carlos"

greeting = "Hello, " + name

# print(greeting)

age = 22
age_as_str = str(age)
# print("you are " + age_as_str)


##############################
## String formatting

name = "Carlos"
greeting = "Hello, " + name


# python 3.6 uses F strings

another_greeting = f"How are you, {name}? I'm very good!"


# Format method
final_greeting = "How are you, {nombre}".format(nombre=name)

friend_name = "Rolf"
goodbye = "Goodbye, {name}"

goodbye_rolf = goodbye.format(name=name)




#######################################
## User input

my_name = "Dias"
# your_name = input("Enter your name: ") # -> Always a string



#######################################
## len, print, input function

# print("Hace print de lo que sea.")
# input("What's your name? ")
# len("Dias")



#######################################
## str, int, float functions

# str convert into a str
# int convert into a int
# float convert into a float

# my_age = input("What's your age?")
# age_next_year = int(my_age) + 1
# print("You will be " + str(age_next_year) + " in a year.")




#######################################
## FLOW CONTROL (Boolean Values) Data Type
# True or False

# Comparison operators
# == Equal to
# != Not Equal to
# < less than
# > greater than
# <= less or equal to
# >= greater or equal to


# Boolean operators (and / or / not)

# True and True -> True
# True and False -> False
# False and True -> False 
# False and False -> False

# True or True -> True
# True or False -> True
# False or True -> True
# False or False -> False

# not True -> False
# not False -> True


# Mixing Boolean and Comparison Operators

(4 < 5) and (5 < 6)
# True and True -> True

(7 < 5) and (5 < 6)
# False and True -> False

(7 < 5) or (5 < 6)
# False or True -> True


((10 < 5) and (15 < 6)) or ((10 < 5) or (15 > 12))





######################
# Elements of flow control

# Conditions
# Conditions always evaluate down to a Boolean value, True or False.


# Block of code

# Blocks begin with identation increases.
# Blocks can contain other blocks.
# Blocks end when the indentation decreases to zero or to a containing block's indentation.

# name = "Mary"
# password = "swordfish"
# if name == "Mary":
#     print("Hello, Mary")

#     if password == "swordfish":
#         print("Access granted.")
#     else:
#         print("Wrong password")




################################
## Flow control statements


# if statements
name = "Mary"

# if name == "Alice":
#     print("Hi, Alice")
# else:
#     print("Hello, stranger")

# elif statements

age = 1000

# if name == "Alice":
#     print("Hi, Alice")
# elif age < 12:
#     print("You are not Alice")
# elif age > 2000:
#     print("Unlike you, Alice is not that old.")
# elif age > 100:
#     print("You are not Alice.")
# else: 
#     print("else must come at the end.")



##############################
## While Loops


# spam = 0
# if spam < 5:
#     print("Hello, World!")
#     spam = spam + 1

# spam = 0
# while spam < 5:
#     print("Hello, World!")
#     spam = spam + 1

# name = ""
# while name != "your name":
#     name = input("Please type your name. \n")

# print("thank you")


# Loop Infinito
# count = 1
# while True:
#     print(str(count) + " counts")
#     count = count + 1


# Break statements
# while True:
#     name = input("Please type your name. \n")
#     if name == "your name":
#         print("Terminando while loop...")
#         break
    
#     print("Hey, " + name)

# print("Thank you.")


# Continue Statements

# With continue statements we go back to the beggining of the loop

# while True:
#     name = input("Who are you?")

#     if name != "Carlos":
#         continue

#     password = input("Hello, Carlos, What is the password? (It is a fish) ")

#     if password == "swordfish":
#         break

# print("Thank you")


#######################################
## Truthy and falsy values

# "" (string) -> False
# 0 (int) -> False
# 0.0 (float) -> False

name = ""
# not False -> True
# while not name:
#     name = input("Enter your name: ")

# num_of_guests = int(input("How many guests will you have?"))

# if num_of_guests:
#     print("Be sure to have enough room for all your guests.")



#######################################
## For loops and range function

# count = 0
# while count < 5:
#     print(str(count) + " Hello, World!")
#     count = count + 1

# for i in range(5):
#     print(f"{i} Hello, World!")


# NOTE: You can use BREAK and CONTINUE statements inside FOR loops as well.

# for i in range(5):
#     if i == 2:
#         continue
#     elif i == 3:
#         break
    
#     print(f"{i} Hello, World!")


######################################
## Start, Stop, Step (range function)

# range(start, stop, step)



#####################################
## import modules


import random

n = random.randint(1, 10)

from random import randint

n = randint(1, 10)


##################################
## Ending a program with sys.exit() function

from sys import exit

while True:
    response = input("Type 'exit' to exit.\n")
    if response == "exit":
        exit()
    print(f"You typed {response}")

print("Goodbye")


#######################################
## Rock Paper Scissors program

# HINT: use random, while true

