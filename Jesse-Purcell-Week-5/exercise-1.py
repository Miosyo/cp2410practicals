def recursive_fib(n):
    if n <= 1:
        return n
    return recursive_fib(n - 1) + recursive_fib(n - 2)


print(recursive_fib(35))


def cached_fib(n, cache=dict()):  # Cache should be set to dict() not None
    """ 
    Return the nth Fibonacci number.
    :param n: the index of the Fibonacci number to be returned
    :param cache: previously computed numbers
    """
    if n in cache:
        return cache[n]
    elif n <= 1:
        return n
    else:
        cache[n] = cached_fib(n - 1) + cached_fib(n - 2)
        return cache[n]


print(cached_fib(35))
