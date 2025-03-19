'''Used inside nested functions to modify a variable in the outer function.'''


def outer():
    x = 5
    def inner():
        nonlocal x
        x = 10
    inner()
    print(x)  # Output: 10

outer()
