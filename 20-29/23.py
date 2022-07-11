"""

Question:
Write a method which can calculate square value of number
    
"""

def calc_square(number:int) -> None:
    square = number**2
    print(square)

def main():
    num = int(input("Please give number to square: "))
    calc_square(num)

if __name__ == '__main__':
    main()