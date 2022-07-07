"""
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program: hello world! 123

Then, the output should be:
LETTERS 10
DIGITS 3
"""

def letter_calc():
    user_input = list(input("Give me letters and numbers: "))

    digits = 0
    letters = 0

    for d in user_input:
        if d.isalpha() == True:
            letters += 1
        else:
            digits += 1

    print(f'LETTERS {letters} \nDIGITS {digits}')

letter_calc()
