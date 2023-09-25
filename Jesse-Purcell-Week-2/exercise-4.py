def binary_search(data_list, target):
    low = 0
    high = len(data_list) - 1  # the -1 fixes the array out of bounds exception
    while low < high:
        # This code does integer division instead of normal division
        mid = (low + high) // 2
        if data_list[mid] < target:
            low = mid + 1
        elif data_list[mid] > target:
            high = mid - 1
        else:
            return mid
    return None


print(binary_search([], 42))  # outputs: None
print(binary_search([1, 2, 3, 4, 5], 3))  # outputs: 2
print(binary_search([1, 2, 3, 4, 5], 6))  # outputs: None
print(binary_search([1, 2, 3, 4, 5], 0))  # outputs: None
