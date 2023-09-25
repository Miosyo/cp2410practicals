import random
import sys

def find_max(numbers):
    """_summary_

    Args:
        numbers (_type_): _description_

    Returns:
        _type_: _description_
    """
    max_number = None
    for number in numbers:
        if max_number == None or number > max_number:
            max_number = number
    return max_number
    # the Big-O notation category for this algorithm is O(n)
    # the category is linear
    
numbers = []
print(find_max(numbers)) # Output None

numbers = [2, 3, 5, 7, 11]
print(find_max(numbers)) # Output 11

numbers = [22, 22, 22, 22, 500]
print(find_max(numbers)) # Output 500

numbers = []
for i in range(0, 10000):
    numbers.append(random.randint(0, 100))
print(find_max(numbers)) # Output 100 most of the time


def find_min(numbers):
    """_summary_

    Args:
        numbers (int[]): _description_

    Returns:
        int: _description_
    """
    min_number = None
    for number in numbers:
        if min_number == None or number > min_number:
            min_number = number
    return min_number
    # the Big-O notation category for this algorithm is O(n)
    # the category is linear
    
numbers = []
print(find_min(numbers)) # Output sys.maxsize

numbers = [2, 3, 5, 7, 11]
print(find_min(numbers)) # Output 2

numbers = [22, 22, 22, 22, 5]
print(find_min(numbers)) # Output 5

numbers = []
for i in range(0, 10000):
    numbers.append(random.randint(0, 100))
print(find_min(numbers)) # Output 0 most of the time