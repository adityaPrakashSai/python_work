# defines skeleton of an algorithm in superclass
# but lets subclasses override specific steps of the algo
# without changing its structure

from abc import ABC, abstractmethod

class AbstractClass(ABC):
    """
    Abstract class defines a template method that contains a skeleton of some algorithm,
    composed of calls to abstract primitive operations

    Concrete subclasses should implement these operations, but leave the template method itself
    intact
    """

    def template_method(self) -> None:
        """
        the template method defines the skeleton of the algorithm
        """
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    def base_operation1(self) -> None:
        print("AbstractClass: I am doing bulk of the work")
    
    def base_operation2(self) -> None:
        print("AbstractClass: But I let the subclasses override some operations")
    
    def base_operation3(self) -> None:
        print("Abstract Class: But I am doing the bulk of the work anyway")

    # these operations have to be implemented in subclasses

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    # these are hooks. subclasses may override them, it is not mandatory. Since the hooks already have default
    # implementation. Hooks provide additional extension points in some crucial places of the algorithm

    def hook1(self) -> None:
        pass
    def hook2(self) -> None:
        pass

class ConcreteClass1(AbstractClass):
    """
    Concrete classes have to implement all abstract operations of the base class.
    They can also override some operations with a default implementation
    """

    def required_operations1(self) -> None:
        print("ConcreteClass1: Implemented Operation1")
    
    def required_operations2(self) -> None:
        print("ConcreteClass1: Implemented Operation2")
    
class ConcreteClass2(AbstractClass):
    """
    Usually concrete classes override only a fraction of base class operations
    """

    def required_operations1(self) -> None:
        print("ConcreteClass2: Implemented Operation1")
    
    def required_operations2(self) -> None:
        print("ConcreteClass2: Implemented Operation2")
    
    def hook1(self) -> None:
        print("ConcreteClass2: Overridden hook1")

def client_code(abstract_class: AbstractClass) -> None:
    """
    the client code calls the template method to execute the algorithm. Client code
    does not have to know the concrete class of an object it works with, as lons as it works 
    with objects through the interface of their base class
    """

    abstract_class.template_method()

if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass1())
    print("\n")
    client_code(ConcreteClass2())
