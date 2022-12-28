"""
* What is this pattern about ?

In Java and many other languages, the abstract factory pattern serves to provide an interface for creating
related / dependent objects without need to specify their actual class

The idea is to abstract the creation of objects depending on business logic, platform choice, etc

In Python, the interface we use is simply a callable, which is "builtin" interface
in python and in normal circumstances we can simply use the class itself as that callable, because classes are
first class objects in python.

* What does this example do ?

This particular implementation abstracts the creation of a pet and does so depending on the factory we chose 
(dog, cat or random animal). This is because both dog, cat and random animal respect a common interface.

*TL;DR
Provides a way to encapsulate a group of individual factories
"""

import random
from typing import Type

class Pet:
    def __init__(self, name: str) -> None:
        self.name = name
    
    def speak(self) -> None:
        raise NotImplementedError
    
    def __str__(self) -> str:
        raise NotImplementedError

class Dog(Pet):
    def speak(self) -> None:
        print("woof")

    def __str__(self) -> str:
        return f"Dog<{self.name}>"

class Cat(Pet):
    def speak(self) -> None:
        print("meow")
    
    def __str__(self) -> str:
        return f"Cat<{self.name}>"

class PetShop:
    def __init__(self, animal_factory: Type[Pet]) -> None:
        self.pet_factory = animal_factory
    
    def buy_pet(self, name: str) -> Pet:
        pet = self.pet_factory(name)
        print(f"Here is your lovely {pet}")
        return pet

def random_animal(name: str) -> Pet:
    return random.choice([Dog, Cat])(name)

def main() -> None:
    shop = PetShop(random_animal)
    for name in ["Max", "Jack", "Buddy"]:
        pet = shop.buy_pet(name)
        pet.speak()
        print("=" * 20)

if __name__ == "__main__":
    random.seed(568)
    main()