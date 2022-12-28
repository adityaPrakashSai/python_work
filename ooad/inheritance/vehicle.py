# Base class (Parent)
class Vehicle():
    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    def get_name(self):
        print("The car is a", self.name, self.model, end="")

# Single inheritance
# Fuel car class extending from vehicle class
# Derived class (Child)
class FuelCar(Vehicle):
    def __init__(self, name, model, combust_type):
        self.combust_type = combust_type
        Vehicle.__init__(self, name, model)

    def get_fuel_car(self):
        super().get_name()
        print(", combust type is", self.combust_type, end="")

# Hierarchical inheritance
# along side the fuel car class, the electric car class is also extending from Vehicle class
# Another derived class

class ElectricCar(Vehicle):
    def __init__(self, name, model, battery_power):
        self.battery_power = battery_power
        super().__init__(name, model)
    
    def get_electric_car(self):
        super().get_name()
        print(", battery power is", self.battery_power, end="")

# Multilevel inheritance
# Gasoline class is derived from the Fuel car class, which is further derived from the vehicle class
# derived class (Grand child)

class GasolineCar(FuelCar):
    def __init__(self, name, model, combust_type, gas_capacity):
        self.gas_capacity = gas_capacity
        FuelCar.__init__(self, name, model, combust_type)
    
    def get_gasoline_car(self):
        super().get_fuel_car()
        print(", gas capacity is", self.gas_capacity, end="")

# Multiple inheritance
# the hybridcar class is derived from two different classes, the gasoline car class and the electric car class
# derived class

class HybridCar(GasolineCar, ElectricCar):
    def __init__(self, name, model, combust_type, gas_capacity, battery_power):
        GasolineCar.__init__(self, name, model, combust_type, gas_capacity)
        ElectricCar.__init__(self, name, model, battery_power)
        self.battery_power = battery_power
    
    def get_hybrid(self):
        self.get_gasoline_car()
        print(", battery power is", self.battery_power)

def main():
    print("Single inheritance:")
    fuel_car = FuelCar("Honda", "Accord", "Petrol")
    fuel_car.get_fuel_car()
    print("\n")

    print("Hierarchical inheritance:")
    electric_car = ElectricCar("Tesla", "ModelX", "200MWH")
    electric_car.get_electric_car()
    print("\n")

    print("Multilevel inheritance: ")
    gasoline_car = GasolineCar("Toyota", "Corolla", "Gasoline", "30 liters")
    gasoline_car.get_gasoline_car()
    print("\n")

    print("Multiple Inheritance: ")
    hybrid_car = HybridCar("Tyota", "Prius", "Hybrid", "30 liters", "100MWH")
    hybrid_car.get_hybrid()

main()


    