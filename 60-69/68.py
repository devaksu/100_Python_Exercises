"""
Please write a binary search function which searches an item in a sorted list. 
The function should return the index of element to be searched in the list.

"""

from bisect import bisect_left

un_sorted = [12,52,37,9,1091,7,222]

# Using bisect
def bisect_binary_search(array:list[int], target) -> int:
    array.sort()
    index = bisect_left(array, target)
    if index < len(array) and array[index] == target:
        return index
    
#Iterative
def binary_search(array:list[int], target:int) -> int:
    array.sort()
    left, right = 0, len(array)-1
    
    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid

        if array[mid] < target:
            left = mid + 1

        elif array[mid] > target:
            right = mid - 1


def main():
    print(bisect_binary_search(un_sorted,222))
    print(binary_search(un_sorted,222))


if __name__ == '__main__':
    main()
