from tail_recursive import tail_recursive


def fibonacci(n):
    # This algorithm has a time complexity of O(2^n)
    # # Also known as "Exponential time"
    print("Computing fibonacci({})".format(n))
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(3))  # outputs: 55
print(fibonacci(20))  # outputs: 6765
print(fibonacci(30))  # outputs: 832040
print(fibonacci(40))  # outputs: 102334155
print(fibonacci(50))  # outputs: 12586269025


@tail_recursive()
def fib(n, a=0, b=1):
    # Computes the nth Fibonacci number
    # This functions time complexity is O(n) linear time!
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fib.tail_call(n-1, b, a+b)


print(fib(10))  # outputs: 55
print(fib(20))  # outputs: 6765
print(fib(30))  # outputs: 832040
print(fib(40))  # outputs: 102334155
print(fib(50))  # outputs: 12586269025
