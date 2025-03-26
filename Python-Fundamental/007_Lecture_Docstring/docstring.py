
""" Docsring is a string that is written in the first line of a class or function
Type of Docstring:
1. Single Line Docstring
2. Multi Line Docstring
3. Triple Double Quote Docstring
"""


# Single Line Docstring
def Hello():
    """This function print Hello World"""
    print("Hello World")

Hello()

# Multi Line Docstring
def AddTwoValue(n1,n2):
    """This function accept two args for n1 and n2"""
    return n1 + n2

print(AddTwoValue(2,5))

# Triple Double Quote Docstring
def SubTwoValue(n1,n2):
    """This function accept two args for n1 and n2
    and return the substracted value"""
    return n1 - n2

print(SubTwoValue(5,2))

# Class Docstring

class UseDocstring:
    
    def Hello(self):
        """This class accept two args for example"""
        print("Hello World")

    def AddTwoValue(self,n1,n2):
        """This class accept two args for n1 and n2"""
        return n1 + n2



use1 = UseDocstring()
use1.Hello()

print(use1.AddTwoValue(2,5))



# Single Quote Docstring
def Hello():
    '''This function print Hello World'''
    print("Hello World")

Hello()

# Double Quote Docstring
def Hello():
    """This function print Hello World"""
    print("Hello World")
    
Hello()