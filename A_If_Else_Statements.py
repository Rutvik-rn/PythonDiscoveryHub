"""
In Python, if-else statements are used to make decisions in your code based on whether a given condition is True or False
An if else statement in Python runs as shown in the syntax below:

if condition:
    code to execute if the condition is True
else:
    code to execute if the condition is False

In the program below, the if-else statement is used to determine whether a user is eligible to vote based on their age. 
The if block is executed when the condition user_age >= 18 is True, and the else block is executed when the condition is False.
"""

user_age = int(input("Enter your age: "))
if user_age >= 18:
    print("You are eligible to vote!")
else:
    print("Sorry, you are not eligible to vote yet.")

# Now we will see something called as nested loops:
""" Let's say you want to check wheter the person is citizen of a particular country and is above 18 then only the person can vote.
The Syntax for Nested Loops:
if condition:
    another if condition:
        code to execute if the condition is True
    else:
        code to execute if condition is False
else:
    code to execute if condition is False

"""

user_age = int(input("Enter your age: "))


if user_age >= 18:
    user_country = input("Enter Your Country Name: ")
    country_upper = user_country.upper()  # this converts the string entered by user to UPPERCASE
    if country_upper == ('INDIA'):
        print("You are a citizen of this country. You are eligible to vote!")
    else:
        print("You are not a citizen of this country, Sorry you are not allowed to vote!")
else:
    print("Sorry, you are not eligible to vote yet.")