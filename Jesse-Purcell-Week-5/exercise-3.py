factorial_cache = dict()


def factorial(n):
    # if n is 0 or 1, return 1 since 0! = 1! = 1
    if n <= 1:
        return 1

    # If we calculated factorial(n) before, return the cached value
    if n in factorial_cache:
        print(f"Using cached factorial of {n}")
        return factorial_cache[n]

    # Otherwise, calculate factorial(n) and store it in the cache
    else:
        result = n * factorial(n - 1)
        factorial_cache[n] = result
        return result


print(factorial(10))
print(factorial(20))
print(factorial(30))
