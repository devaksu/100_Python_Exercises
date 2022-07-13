"""
Write a function to compute 5/0 and use try/except to catch the exceptions.
"""

def func54():
    try:
        a = 5/0
        print(a)
    except ZeroDivisionError:
        print('ZeroDivisionError occurred')
    finally:
        print("Printing something")