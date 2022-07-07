"""
Question:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.

Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9

Then, the output should be:
1,3,5,7,9...
"""
user_input = input("Please give numbers separeted by comma: ").split(',')
old_list = [1,2,3,4,5,6,7,8,9]

def square_comprehension(input: list[str]) -> None:

    squares = [s for s in input if int(s) % 2 == 1]
    print(','.join(squares))


square_comprehension(user_input)