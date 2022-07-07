"""
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:
Hello world!

Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""

def lettercase_calc():
    user_input = list(input("Give me letters or phrase: "))

    lower = 0
    upper = 0

    for d in user_input:
        if d.isupper() == True:
            upper += 1
        
        elif d.islower() == True:
            lower += 1

        elif d.isspace() == True:
            pass
 
        else:
            raise ValueError("No idea of one of characters")
            

    print(f'UPPERS {upper} \nLOWERS {lower}')

lettercase_calc()