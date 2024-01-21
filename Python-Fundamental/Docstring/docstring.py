
"""This is we call docsting"""
"""Use docstring to display info of class or function using, it show when we calling class or method its self and hover on it"""

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



