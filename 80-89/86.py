"""
Question:
Please write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program: abcdefgabc

Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1
"""

def char_calc(string:str) -> dict[str,int]:
    char_list = list(string.lower())
    chars = {}
    for c in char_list:
        if c in chars:
            chars[c] += 1
        
        else:
            chars[c] = 1
    not_chars = [" ", "'", ",",".", "!", "?"]
    for a in not_chars:
        if a in chars:
            chars.pop(a)

    keys = sorted(chars.keys())

    for c in keys:
        print(f'{c},{chars[c]}')


char_calc("Shot through the heart And you're to blame Darlin', you give love a bad name!")