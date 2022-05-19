# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward.
#
# For example, 121 is a palindrome while 123 is not.
# Follow up: Could you solve it without converting the integer to a string?
def is_palindrome():
    input_number = int(input('Enter a number: '))
    initial_number = input_number
    revs_number = 0
    while input_number > 0:
        remainder = input_number % 10
        revs_number = (revs_number * 10) + remainder
        input_number = input_number // 10
    print(f"The reversed number of {initial_number} is {revs_number}")

    if initial_number == revs_number:
        return True
    else:
        return False