"""
Question:
Define a function that can accept two strings as input and print the string with maximum length in console. 
If two strings have the same length, then the function should print all strings line by line.
"""

def longer_str(string1:str, string2:str) -> str:
    length1 = len(string1)
    length2 = len(string2)

    if length1 == length2:
        print(f'{string1}\n{string2}')

    elif length1 > length2:
        print(f'{length1} words: {string1}')
    
    else:
        print(f'{length2} words: {string2}')

longer_str('Happy birthday!','Happy birthday')
longer_str('Happy birthday1','Happy birthday11')
longer_str('Happy birthday','Happy birthday')
