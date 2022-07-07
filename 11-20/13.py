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
        
        elif d.isdigit() == True:
            digits += 1

        elif d.isspace() == True:
            pass 
          
        else:
            raise ValueError("No idea of one of characters")
            

    print(f'LETTERS {letters} \nDIGITS {digits}')

letter_calc()
