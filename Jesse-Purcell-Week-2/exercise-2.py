import random


def find_index_of_smallest(data_list):
    smallest = None
    for i in range(len(data_list)):
        if not smallest or data_list[i] < data_list[smallest]:
            smallest = i
    return smallest
# O(n)


print(find_index_of_smallest([1, 2, -8, 0, 5, 6, 10]))  # outputs: 2
print(find_index_of_smallest([1, 2, -8, 0, 5, 6, 10, -100]))  # outputs: 7
print(find_index_of_smallest([]))  # outputs: None
print(find_index_of_smallest(
    [1, 2, 3, 0, 4, 5, 6, 7, 8, 0, 9, 10]))  # outputs: 3

input_list = []
for i in range(100_000):
    input_list.append(random.randint(-100, 100))

# To tell if the code is working in this test case
print(find_index_of_smallest(input_list))
# You would either print out the list and manually check or return the value at the index and check to
# see if it was -100 as the chances of -100 not being generated in a list of 100_000 numbers
# is very slim


def find_smallest(data_list):
    smallest = data_list[0]
    for i in data_list:
        if i < smallest:
            smallest = i
    return smallest
# O(n)


def find_indices_of_smallest(data_list):
    if not data_list:
        return None
    smallest = find_smallest(data_list)
    smallest_list = []
    for i in range(len(data_list)):
        if data_list[i] == smallest:
            smallest_list.append(i)
    return smallest_list
# O(n)


print(find_indices_of_smallest([1, 2, -8, 0, 5, 6, 10]))  # outputs: 2
print(find_indices_of_smallest(
    [1, 2, -8, 0, -100, 6, 10, -100]))  # outputs: 4, 7
print(find_indices_of_smallest([]))  # outputs: None
print(find_indices_of_smallest(
    [1, 2, 3, 0, 4, 5, 6, 7, 8, 0, 9, 10]))  # outputs: 3, 9

input_list = []
for i in range(100_000):
    input_list.append(random.randint(-100, 100))

# To check that this test works
print(len(find_indices_of_smallest(input_list)))
# The length of the array should average 500 (100_000 // 200)
