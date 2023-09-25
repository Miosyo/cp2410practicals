import timeit
import random
import matplotlib.pyplot as plt
import math


def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def find_index_of_smallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selection_sort(array):
    original_array = array
    sorted_array = []
    for i in range(len(original_array)):
        smallest = find_index_of_smallest(original_array)
        sorted_array.append(original_array.pop(smallest))
    return sorted_array


def quick_sort(array):
    if len(array) < 2:  # return the base case
        return array
    else:
        pivot_index = len(array) // 2
        pivot = array[pivot_index]
        less = [i for i in array if i < pivot]
        greater = [i for i in array if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def bubble_sort_optimized(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return arr
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Splitting the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive calls to merge_sort() for both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merging the two sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Comparing elements from left and right halves and adding them to merged
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Adding any remaining elements from the left or right halves
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def run_benchmark(algorithm, data_list): return timeit.timeit(
    lambda: algorithm(data_list), number=10)


x = [length for length in range(1, 1001, 100)]

y_selection_sort = []
y_quick_sort = []
y_bubble_sort = []
y_bubble_sort_optimized = []
y_merge_sort = []
y_insertion_sort = []

for length in x:
    data_list = [random.randint(1, 101) for number in range(length)]

    result = run_benchmark(selection_sort, data_list[:])
    y_selection_sort.append(result)

    result = run_benchmark(quick_sort, data_list[:])
    y_quick_sort.append(result)

    result = run_benchmark(bubble_sort, data_list[:])
    y_bubble_sort.append(result)

    result = run_benchmark(bubble_sort_optimized, data_list[:])
    y_bubble_sort_optimized.append(result)

    result = run_benchmark(merge_sort, data_list[:])
    y_merge_sort.append(result)

    result = run_benchmark(insertion_sort, data_list[:])
    y_insertion_sort.append(result)

plt.plot(x, y_selection_sort, label='selection sort')
plt.plot(x, y_quick_sort, label='quick sort')
plt.plot(x, y_bubble_sort, label='bubble sort')
plt.plot(x, y_bubble_sort_optimized, label='bubble sort optimized')
plt.plot(x, y_merge_sort, label='merge sort')
plt.plot(x, y_insertion_sort, label='insertion sort')
plt.ticklabel_format(style='plain')
# plt.ylim(0, 0.1)
# plt.xscale('log')
# plt.yscale('log')
plt.xlabel('n')
plt.ylabel('time (seconds)')
plt.title('Running Times')
plt.legend()
plt.show()
