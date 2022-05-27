#!/usr/bin/env python3

print("Simple CLI Calculator")

while (True):
    try:
        user_input1 = int(input("Enter a number (OR ANY ALPHABETIC CHARACTERS TO EXIT): "))
    except:
        print("You EXITED the calculator.")
        break

    user_input2 = input("Which operation to perform? (+, -, *, /): ")

    try:
        user_input3 = int(input("Enter another number (OR ANY ALPHABETIC CHARACTERS TO EXIT): "))
    except:
        print("You EXITED the calculator.")
        break

    if (user_input2 == "+"):
        print(f"{user_input1} + {user_input3} = {user_input1 + user_input3}")

    if (user_input2 == "-"):
        print(f"{user_input1} - {user_input3} = {user_input1 - user_input3}")

    if (user_input2 == "*" ):
        print(f"{user_input1} * {user_input3} = {user_input1 * user_input3}")

    if (user_input2 == "/") :
        print(f"{user_input1} / {user_input3} = {user_input1 / user_input3}")