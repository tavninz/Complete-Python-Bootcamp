'''A function calling itself is called recursion.
'''


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120