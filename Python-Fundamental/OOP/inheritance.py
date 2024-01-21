class Model:
    def SayModel(self):
        print("Model!!!")
        
    def SaySpeed(self):
        print("Speed!!!")
        
    
class Apple(Model):
    
    def SayApple(self):
        print("Apple!!!")
        
        

m1 = Apple()

m1.SayModel()
m1.SaySpeed()
m1.SayApple()