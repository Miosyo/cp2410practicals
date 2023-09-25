import random

def binary_search(list, item):
    """_summary_

    Args:
        list (int):
        item (int):

    Returns:
        int: _description_
    """
    print(f"binary search, list: {list} item: {item}")
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        print(f"low: {low}")
        print(f"high: {high}")
        guess = list[mid]
        print(f"guess: {guess}")
        if guess == item:
            return mid
        if guess > item:
            print("guess is greater than item")
            high = mid - 1
        else:
            print("guess is less than item")
            low = mid + 1
    print("item not found")
    return None


my_list = [1, 3, 5, 7, 9]
print("result: " + str(binary_search(my_list, 3)))
print("result: " + str(binary_search(my_list, -1)))

numbers = random.sample(range(1, 100000), 1000)  # Creates a random list of values from an input pool of values
# print(numbers)
print("result: " + str(binary_search(numbers, 42)))
print("result: " + str(binary_search(numbers, 1000000)))
print("result: " + str(binary_search(numbers, 1)))
print("result: " + str(binary_search(numbers, 99999)))
print("result: " + str(binary_search(numbers, -1)))
# The list isn't sorted sorted and binary search will not work

numbers.sort()
print("result: " + str(binary_search(numbers, 42)))
print("result: " + str(binary_search(numbers, 1000000)))
print("result: " + str(binary_search(numbers, 1)))
print("result: " + str(binary_search(numbers, 99999)))
print("result: " + str(binary_search(numbers, -1)))
# The list is sorted