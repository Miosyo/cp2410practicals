import random

def calculate_average(numbers):
    """_summary_

    Args:
        numbers (_type_): _description_

    Returns:
        _type_: _description_
    """
    if len(numbers) == 0: return None
    return sum(numbers) / len(numbers)
    # the Big-O notation category for this algorithm is O(n)
    # although the way I've written it probably makes in O(2n) as it checks the list a second time to get the size of the list
    # the category is linear

numbers = []
print(calculate_average(numbers)) # Output None

numbers = [2, 3, 5, 7, 11]
print(calculate_average(numbers)) # Output 5.6

numbers = [22, 22, 22, 22, 500]
print(calculate_average(numbers)) # Output 117.6

numbers = []
for i in range(0, 10000):
    numbers.append(random.randint(0, 100))
print(calculate_average(numbers)) # Output something close to 50