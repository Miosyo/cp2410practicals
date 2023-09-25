from exercise_1 import *
from exercise_2 import *


def knapsack(items, max_size):
    # create the dynamic programming grid
    grid = [[0 for i in range(max_size + 1)] for j in range(len(items) + 1)]
    # populate dynamic programming grid
    for i in range(1, len(items) + 1):
        item_value = items[i - 1]['value']
        item_size = items[i - 1]['size']

        for j in range(1, max_size + 1):
            # if the item can't fit, carry over the value from the cell above
            if item_size > j:
                grid[i][j] = grid[i - 1][j]
            else:
                # if the item can fit, choose the maximum between
                # - The value of the current item + the value of the remaining column from previous
                # - The value from the cell directly above
                grid[i][j] = max(item_value + grid[i - 1]
                                 [j-item_size], grid[i-1][j])

    # find the selected items
    selected_items = []

    i = len(items)
    j = max_size
    while i > 0 and j > 0:
        if grid[i][j] != grid[i - 1][j]:
            selected_items.append(items[i-1]['name'])
            j -= items[i - 1]['size']
        i -= 1
    return grid[-1][-1], selected_items


def display_items(items):
    for item in items:
        print(f"{item['name']} - ${item['value']} - {item['size']}kg")
    print()


if __name__ == '__main__':
    names = {
        'ring',
        'watch',
        'coins',
        'vase',
        'painting',
        'statue',
        'lamp',
        'book',
        'bottle',
        'sculpture',
        'cards',
        'gun',
        'medal',
        'stamp',
        'doll'
    }

    qualifiers = {
        'old',
        'ancient',
        'special',
        'rare',
        'unique',
        'small',
        'large',
        'tiny',
        'big',
        'huge',
        'classic',
        'art deco',
        'modern',
        'vintage',
        'antique'
    }

    max_size = 225

    for size in range(2, max_size + 1):
        print(f"Generating items with size = {size}:")
        items = list(generate_items(size, names, qualifiers))
        # print(items)
        display_items(items)

        best_value, selected_items = knapsack(items, size)
        print('Dynamic programming solution:')
        print(f"Best Value: {best_value}")
        print(f"Selected Items: ", end='')
        print(*selected_items, sep=', ')
        print()
