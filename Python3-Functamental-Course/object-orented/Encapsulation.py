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