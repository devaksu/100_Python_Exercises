"""
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

def are_digits_even(lower: int=1000, upper: int=3000) -> None:
    all_digits_even = []
    for number in range(lower,upper+1):     # Iterate through all numbers
        s = str(number)
        for i in range(len(s)):             # Iterate through all digits in number
            flag = []
            if int(s[i]) % 2 == 1:
                flag.append(False)
                break
            else:
                flag.append(True)
        
        if False in flag:                   # If list contains any Falses
            continue
        else:
            all_digits_even.append(s)

    print(",".join(all_digits_even))


are_digits_even()