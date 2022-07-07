"""
Question:
Write a program that accepts a comma separated sequence of words as input and 
prints the words in a comma-separated sequence after sorting them alphabetically.

Example: 
Suppose the following input is supplied to the program:
without,hello,bag,world

Then, the output should be:
bag,hello,without,world
"""

def main():
    word_list = input("Please give a comma separated sequence of words: ").split(',')
    processed_list = []
    for word in word_list:
        processed_list.append(word.strip())

    print(','.join(sorted(processed_list)))
    

main()