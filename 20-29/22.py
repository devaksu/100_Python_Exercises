"""
Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
"""

def main():
    freqs = {}
    words = input("Please provide sentence to calculate word frequency: ").split()
    for word in words:
        freqs[word] = freqs.get(word,0)+1

    word_list = list(freqs.keys())
    word_list.sort()

    for w in word_list:
        print(f'{w}:{freqs[w]}')

main()