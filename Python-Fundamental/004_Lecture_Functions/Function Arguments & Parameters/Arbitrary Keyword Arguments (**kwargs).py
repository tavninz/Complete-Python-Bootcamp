'''Used when an unknown number of keyword arguments is passed.'''


def person_info(**info):
    return f"Name: {info['name']}, Age: {info['age']}"

print(person_info(name="Alice", age=30))  # Output: Name: Alice, Age: 30