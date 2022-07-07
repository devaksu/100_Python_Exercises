"""
Question:
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:
Hello world
Practice makes perfect

Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

"""
def get_lines():
    lines = []
    while True:
        l = input("Give me a line: ")
        if l:
            lines.append(l)
        else:
            break
    
    return lines


def upper_case(lines: list[str]) -> list[str]:
    upper_lines = []
    for line in lines:
        upper_lines.append(line.upper())
    
    return upper_lines

def main():
    lines = get_lines()
    uppers = upper_case(lines)
    for line in uppers:
        print(line)

main()
