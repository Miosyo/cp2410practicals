import matplotlib.pyplot as plt
import math


factorial_cache = dict()


def factorial(n):
    # if n is 0 or 1, return 1 since 0! = 1! = 1
    if n <= 1:
        return 1
    if n in factorial_cache:
        return factorial_cache[n]
    result = n * factorial(n - 1)
    factorial_cache[n] = result
    return result


x = [length for length in range(1, 101, 1)]

y_log_n = [math.log(n, 2) for n in x]
y_n = [n for n in x]
y_n_log_n = [n * math.log(n, 2) for n in x]
y_n_square = [n ** 2 for n in x]
y_n_exp = [2 ** n for n in x]
# Can't use large factorial numbers
y_n_factorial = [factorial(n) for n in x]

plt.plot(x, y_log_n, label='log(n)')
plt.plot(x, y_n, label='n')
plt.plot(x, y_n_log_n, label='n log(n)')
plt.plot(x, y_n_square, label='n**2')
plt.plot(x, y_n_exp, label='2**n')
plt.plot(x, y_n_factorial, label='n!')
plt.ticklabel_format(style='plain')
plt.ylim(0, 100)
plt.xlabel('n')
plt.ylabel('f(n)')
plt.title('Big O Notation')
plt.legend()
plt.show()
