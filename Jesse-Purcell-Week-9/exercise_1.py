import itertools


def total_value(combination):
    total_value = 0
    for item in combination:
        total_value += item['value']
    return total_value


def total_weight(combination):
    total_weight = 0
    for item in combination:
        # print(item)
        total_weight += item['size']
    return total_weight


def is_valid(combination, max_size):
    return total_weight(combination) <= max_size


def generate_combinations(items):
    combinations = []
    for i in range(1, len(items) + 1):
        combinations += list(itertools.combinations((items), i))
    return combinations


# Complexity of O(2^n)
def find_best_combination(items, max_size):
    # generate all possible combinations
    combinations = generate_combinations(items)

    # find the best combination
    best_combination = None
    for combination in combinations:
        if is_valid(combination, max_size):
            if best_combination is None:
                best_combination = combination
            elif total_value(combination) > total_value(best_combination):
                best_combination = combination
    return best_combination


def display_solution(solution):
    for item in solution:
        print(f"{item['name']} - ${item['value']} - {item['size']}kg")
    print(f"Total Value: ${total_value(solution)}")
    print(f"Total Weight: {total_weight(solution)}kg")
    print()


if __name__ == '__main__':
    items = [
        {'name': 'Watch', 'value': 3000, 'size': 3},
        {'name': 'Coins', 'value': 2000, 'size': 4},
        {'name': 'Ring', 'value': 1500, 'size': 1},
        {'name': 'Picture', 'value': 2000, 'size': 1},
        {'name': 'Vase', 'value': 2500, 'size': 4},
        {'name': 'Book', 'value': 1500, 'size': 2},
        {'name': 'Sculpture', 'value': 2000, 'size': 2},
        {'name': 'Wine', 'value': 1000, 'size': 2}
    ]

    # Test Code
    assert (total_value((items[0], items[1])) == 5000)
    assert (total_value((items[0], items[2])) == 4500)
    assert (total_weight((items[0], items[1])) == 7)
    assert (total_weight((items[0], items[2])) == 4)
    assert (is_valid((items[0], items[1]), 4) == False)
    assert (is_valid((items[0], items[2]), 4) == True)

    max_size = 10
    for i in range(2, max_size + 1):
        print(f"Max Size: {i}")
        solution = find_best_combination(items, i)
        display_solution(solution)
