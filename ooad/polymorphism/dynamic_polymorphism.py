# dynamic polymorphism is achieved through method overriding
# if a class provides a specific implementation of a method that had already been defined in one of its parent classes it is 
# known as method overriding

class Animal:
    def __init__(self):
        pass

    def print_animal(self):
        print("I am from the animal class")
    
    def print_animal_two(self):
        print("I am from the animal class")

class Lion(Animal):
    def __init__(self):
        super()
    
    def print_animal(self):
        print("I am from the Lion class")
    
lion = Lion()
lion.print_animal()
lion.print_animal_two()
