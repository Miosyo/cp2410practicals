
def count_occurrences(word_list, target_word):
    """
    Returns the number of occurrences of the target_word in word_list
    Args:
        word_list (string[]): List of words
        target_word (string): Target word for search

    Returns:
        int: Occurrences of target_word in word_list
    """
    count = 0
    for word in word_list:
        if word == target_word:
            count += 1
    return count
    # the Big-O notation category for this algorithm is O(n)

word_list = ["the", "cat", "sat", "on", "the", "mat"]
target_word = "the"
print(count_occurrences(word_list, target_word)) # output: 2

target_word = "cat"
print(count_occurrences(word_list, target_word)) # output: 1

word_list = ["the", "cat", "sat", "on", "the", "mat"]
target_word = "dog"
print(count_occurrences(word_list, target_word)) # output: 0