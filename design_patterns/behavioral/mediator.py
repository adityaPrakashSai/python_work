# behavioral design pattern, restricts direct communication
# forces them to collaborate only via a mediator object

# real world: aircraft pilots don't interact with each other
# they speak to air traffic controller

# a possible con is that a mediator object can evolve over time into a god object

from __future__ import annotations
from abc import ABC, abstractmethod

class Mediator(ABC):
    """
    the mediator interface declares a method used by components to notify
    the mediator about various events. the mediator may react to these events and pass the execution
    to other components
    """

    @abstractmethod
    def notify(self, sender: object, event: str) -> None:
        pass

class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component2 = component2
        self._component1.mediator = self
        self._component2.mediator = self
    
    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()

class BaseComponent:
    """
    the base component provides the basic functionality of storing
    a mediator's instance inside component objects
    """
    def __init__(self, mediator : Mediator = None) -> None:
        self._mediator = mediator
    
    @property
    def mediator(self) -> Mediator:
        return self._mediator
    
    @mediator.setter
    def mediator(self, mediator:Mediator) -> None:
        self._mediator = mediator


"""
Concrete components implement various functionalities
they don't depend on other components
they also don't depend on any concrete mediator class
"""

class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component1 does A.")
        self._mediator.notify(self, "A")
    
    def do_b(self) -> None:
        print("Component1 does B.")
        self.mediator.notify(self, "B")

class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component2 does C")
        self.mediator.notify(self, "C")
    
    def do_d(self) -> None:
        print("Component2 does D")
        self.mediator.notify(self, "D")

if __name__ == "__main__":
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2)
    print("Client triggers operation A.")
    c1.do_a()

    print("\n", end="")

    print("Client triggers operation D")
    c2.do_d()