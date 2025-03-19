'''Used when the number of arguments is unknown.'''

def add_numbers(*numbers):
    return sum(numbers)

print(add_numbers(1, 2, 3, 4, 5))  # Output: 15