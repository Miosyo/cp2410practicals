def is_palindrome(word):
    # Time complexity of n?
    # Base case: A word with 0 or 1 character is always a palindrome
    if len(word) < 2:
        return True
    # Check if the first and last chars are the same
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        # Word is not a palindrome
        return False


print(is_palindrome("a"))
print(is_palindrome("ab"))
print(is_palindrome("aba"))
print(is_palindrome("level"))
print(is_palindrome("racecar"))
print(is_palindrome("poker"))


def is_palindrome_stack(word):
    # Time complexity of n?
    stack = []
    # Push each character of the word onto the stack
    for char in word:
        stack.append(char)
    # Build the reversed word by popping characters from the stack
    reversed_word = ""
    while len(stack) != 0:
        reversed_word += stack.pop()
    return word == reversed_word


print("Palindrome using a stack")
print(is_palindrome_stack("a"))
print(is_palindrome_stack("ab"))
print(is_palindrome_stack("aba"))
print(is_palindrome_stack("level"))
print(is_palindrome_stack("racecar"))
print(is_palindrome_stack("poker"))
