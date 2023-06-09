#Factory pattern

class Pizza:
    def __init__(self, name: str, size: str, toppins: list, price: float):
        self.name = name
        self.size = size
        self.toppins = toppins
        self.price = price
    
    def customize_pizza(self, name: str, size: str, toppins: list, price: float):
        self.name = name
        self.size = size
        self.toppins = toppins
        self.price = price
        
    def calculate_price(self):
        return self.price
    
class PizzaFactory:
    def create_pizza(self,type_of_pizza):
        if type_of_pizza == 'Margherita':
            return Pizza('Margherita','Medium',['cheese','tomato'],10.0)
        elif type_of_pizza == 'Peperoni':
            return Pizza('Peperoni','Medium',['cheese','tomato','Peperoni'],11.0)
        elif type_of_pizza == 'Veggie':
            return Pizza('Veggie','Medium',['cheese','tomato','mushrooms'],12.0)
        else:
            raise ValueError("Invalid Pizza")
        

# Facade Pattern
#PizzaOrderFacade will simplifies the process of ordering a pizza.
class PizzaOrderFacade:
    def __init__(self, factory: PizzaFactory):
        self.factory = factory
        
    def order_pizza(self, type_of_pizza):
        pizza = self.factory.create_pizza(type_of_pizza)
        pizza.customize_pizza(pizza.name, pizza.size, pizza.toppins, pizza.price)
        return pizza
    
#Singleton Pattern
class Singleton(type):
    _instance = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instance[cls] = super(Singlenton, cls).__call__(*args,**kwargs)
        return cls._instance[cls]



        