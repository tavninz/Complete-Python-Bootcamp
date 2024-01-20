class Model:
    def ringtone(self):
        print("Model of phone ringtones!!!")
        
class Apple(Model):
    def ringtone(self):
        print("Apple Ringtones!!!")
        
class Sumsong(Model):
    def ringtone(self):
        print("Sumsong Ringtones!!!")
        
        
m1 = Model()
m1.ringtone()

a1 = Apple()
a1.ringtone()

s1 = Sumsong()
s1.ringtone()