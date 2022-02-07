import getpass

# QUESTION 2 #
# Write a Python program that emulates the high-street bank mechanism for checking a #
# PIN. Keep taking input from the keyboard (see below) until it is identical to a password #
# number which is hard-coded by you in the program. #

# make official pin #
official_pin = 2578

# starting amount of attempts left #
tries = [1, 2, 3]
attempts_left = 3

for x in tries:
# could've used a range #

# comment added to test github #

    user_input_str = input("Please enter your PIN: ")
    input_pin = int(user_input_str)

    if input_pin == official_pin:
        print("PIN correct")
        break

    else:
        attempts_left -= 1

        if attempts_left > 0:
            print('PIN incorrect ' + str(attempts_left) + " attempts remaining")

if input_pin != official_pin:
    print("Your card is locked, please try again later")

