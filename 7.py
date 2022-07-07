"""
Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.

Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

"""

def array_gen() -> None:
    X = int(input('Please give a value for X: '))
    Y = int(input('Please give a value for Y: '))
    arr = []

    for i in range(X):
        arr2= []
        for j in range(Y):
            val = i*j
            arr2.append(val)
        arr.append(arr2)
    
    print(arr)
    
array_gen()