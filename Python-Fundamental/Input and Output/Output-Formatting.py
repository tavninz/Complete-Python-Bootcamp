year = 2016
event = 'Referendum'

print(f'Result the {year} {event}!.')


# format string

vote_yes = 42_572_654
vote_no = 43_132_495
percentage = vote_yes / (vote_no + vote_yes)
print('{} YES votes  {}'.format(vote_yes, percentage))
print('\n')
print('{:-9} YES votes  {:2.2%}'.format(vote_yes, percentage))


print(type(str(1/4)))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

# repr() mean add '' quote to wrap your data

# Formatted String Literals

import math
print(f'The value of pi is approximately {math.pi:.3f}.')


"""Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful for making columns line up."""

table = {'Sjoerd': 4127, 'Jack': 40985, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}') # Dcab       ==>      76780 មានន័យថា មាន space ចំនួន 10 ហើយលេខទាំងអស់ត្រូវស្ថិតក្នុងចន្លោះ 10space នឹងហើយ start from right-to-left
                                        # 012345678910  012345678910




# Other modifiers can be used to convert the value before it is formatted. '!a' applies ascii(), '!s' applies str(), and '!r' applies repr():


animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.') # repr() mean add '' quote to wrap your data



"""The = specifier can be used to expand an expression to the text of the expression, an equal sign, then the representation of the evaluated expression:"""

port = 12
count = 18
name = "Syntax Error"

print(f'Debug {port=}, {count=}, {name=}')
# Debug port=12, count=18, name='Syntax Error'


# The String format() Method
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('Debug on port {} Error say "{}!"'.format(port, name))

print('Debug on port {0} Error say "{1}!"'.format(port, name)) #Debug on port 12 Error say "Syntax Error!"
print('Debug on port {1} Error say "{0}!"'.format(port, name)) #Debug on port Syntax Error Error say "12!"

print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))



# If you have a really long format string that you don’t want to split up, it would be nice if you could reference the variables to be formatted by name instead of by position. This can be done by simply passing the dict and using square brackets '[]' to access the keys.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table))




#Readmore https://docs.python.org/3/tutorial/inputoutput.html