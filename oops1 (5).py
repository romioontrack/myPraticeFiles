class Car:
    def __init__(self,type):      # By default Constructor
        self.type = type
        
    @staticmethod
    def start():
        print("Car Started")
        
    @staticmethod
    def stop():
        print("Car Stopped")    
    
class ToyotaCar(Car):
    def __init__(self,name, type):
        super().__init__(type)
        self.name = name
        super().start()      # super() are used to acces the attibuts or function of differnet class
        super().stop()

car1 = ToyotaCar("prius", "electric")
print(car1.type)
        
        