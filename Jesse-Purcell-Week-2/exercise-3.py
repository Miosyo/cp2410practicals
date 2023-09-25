def find_index_of_smallest(data_list):
    smallest = None
    for i in range(len(data_list)):
        if smallest == None or data_list[i] < data_list[smallest]:
            smallest = i
    return smallest
# O(n)


def selection_sort(data_list):
    if not data_list:
        return None
    sorted_list = []
    for i in range(len(data_list)):
        smallest = find_index_of_smallest(data_list)
        sorted_list.append(data_list.pop(smallest))
    return sorted_list


print(selection_sort([1, 2, -8, 0, 5, 6, 10]))
print(selection_sort([1, 2, -8, 0, 5, 6, 10, -100]))
print(selection_sort([]))  # outputs: None
print(selection_sort(
    [1, 2, 3, 0, 4, 5, 6, 7, 8, 0, 9, 10]))
