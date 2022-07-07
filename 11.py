"""
Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input 
and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example: 0100,0011,1010,1001

Then the output should be: 1010
"""

def get_bins() -> list[str]:
    binarys = input("Please give some 4-bit binary numbers separated with comma: ").split(',')
    binaries= []
    for binary in binarys:
        diff = 4 - len(binary)
        if diff < 0:
            pass
        
        elif diff < 4 and diff > 0:
            binary = diff*'0'+ binary
            binaries.append(binary)

        else:
            binaries.append(binary)

    return binaries

def convert_and_check(binaries: list[str]) -> list[str]:
    divisible = []
    for b in binaries:
        if int(b,2) % 5 == 0:
            divisible.append(b)

    return divisible


def main():
    nums = get_bins()
    checked = convert_and_check(nums)
    print(f'Divisible by 5: {",".join(checked)}')

main()
