"""
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""

def digit_calc(dimension: int, a:int):
    m = ''
    for d in range(1,dimension+1):
        m = m+str(d)
        d += 1

    output = int(m) * a
    print(output)

digit_calc(6,9)