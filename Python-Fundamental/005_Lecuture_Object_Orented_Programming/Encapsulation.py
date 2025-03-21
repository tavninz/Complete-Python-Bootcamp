'''Encapulation is the process of restricting access to methods and variables in a class in order to prevent direct modification of the data.
In python, we denote private attributes using underscore as the prefix i.e single _ or double __
'''
class Brand:
    def __init__(self):
        self.__maxprice = 9000
        
    
    def setMaxPrice(self,price):
        self.__maxprice = price
        
    def getMaxPrice(self):
        return self.__maxprice
    
    
    
b1 = Brand()
b1.setMaxPrice(50000)
print(b1.getMaxPrice())