"""
Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words 
after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again

Then, the output should be:
again and hello makes perfect practice world

"""
def main():
    words = input("Please give words separated with space: ").split(' ')
    word_set = set(words)
    word_list = list(word_set)
    output = sorted(word_list)
    print(" ".join(output))
