# imagine a complex object that requires laborious,
# step by step initialization of many fields and nested objects
# such initialization code is usually buried inside a monstrous constructor with lots of parameters
# you coded so many builders

# builder pattern solves the issue by segregating the entire process into 4 roles:
# 1. The product

from abc import ABC, abstractmethod

class Car:
    """ The Product """
    def __init__(self) -> None:
        self.autonomous_driving = None
        self.sunroof = None
        self.fuel = None
    
    def __str__(self):
        output = (f'Autonomous driving: {self.autonomous_driving} |'
        f'Sunroof: {self.sunroof} | Fuel: {self.fuel}')
        return output

# 2. Abstract builder interface
class AbstractCarBuilder(ABC):
    def __init__(self) -> None:
        self.car = None

    def create_new_car(self):
        self.car = Car()
    
    @abstractmethod
    def add_autonomous_driving(self, autonomous_driving):
        pass

    @abstractmethod
    def add_sun_roof(self, sun_roof):
        pass

    @abstractmethod
    def add_fuel(self, fuel):
        pass

# 3. Car builder that inherits the abstract builder and implements the interface,
# provides methods to create components of the product.

class ConcreteCarBuilder(AbstractCarBuilder):
    ''' Actual Car builder '''
    def add_autonomous_driving(self, autonomous_driving):
        self.car.autonomous_driving = autonomous_driving
    
    def add_sun_roof(self, sun_roof):
        self.car.sunroof = sun_roof
    
    def add_fuel(self, fuel):
        self.car.fuel = fuel

# 4. Director: In charge of creating the product, assembling various components and then delivering it.
# director uses a concrete builder object

class Director:
    def __init__(self, builder : AbstractCarBuilder):
        self._builder = builder
    
    def construct_car(self, autonomous_driving = False, sun_roof = False, fuel = 'Electric'):
        self._builder.create_new_car()
        self._builder.add_autonomous_driving(autonomous_driving)
        self._builder.add_sun_roof(sun_roof)
        self._builder.add_fuel(fuel)
        return self._builder.car

def main():
    concreteCarBuilder = ConcreteCarBuilder()
    director = Director(concreteCarBuilder)
    model_one = director.construct_car(True, True, 'Diesel')
    print(model_one)

if __name__ == "__main__":
    main()