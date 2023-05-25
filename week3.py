class Vehicle:
    
    def __init__(self,name,color):
        self.name = name
        self.color = color
        
    def start(self):
        print(f"The {self.name} is starting.")
        
    def stop(self):
        print(f"The {self.name} is stoping.")
        

class Car(Vehicle):
    
    def __init__(self,name,color):
        super().__init__(name,color)
        
    def honk(self):
        print(f"The {self.name} is honking")
        
class Bike(Vehicle):
    
    def __init__(self,name,color):
        super().__init__(name,color)
        
    def pedal(self):
        print(f"The {self.name} is pedaling")
        
class Truck(Vehicle):
    
    def __init__(self,name,color):
        super().__init__(name,color)
        
    def load(self):
        print(f"The {self.name} is loading")
        
def test_vehicles():
    car = Car("Car","Red")
    bike = Bike("Bike","Blue")
    truck = Truck("Truck","Black")
    
    car.start()
    car.honk()
    car.stop()
    
    truck.start()
    truck.load()
    truck.stop()
    
    bike.start()
    bike.pedal()
    bike.stop()

        
test_vehicles()
        

        
