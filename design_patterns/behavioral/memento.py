# this design pattern lets us save and restore the 
# previous state of an object without revealing the details of its implementation

from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits

class Originator():
    """
    the originator holds some important state that may change over time
    it also defines a method for saving the state inside a memento.
    and another method for restoring the state later
    """

    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        print(f'Originator: My initial state is: {self._state}')
    
    def do_something(self) -> None:
        print("Originator: I am doing something important.")
        self._state = self._generate_random_string(30)
        print(f"Originator: and my state has changed to: {self._state}")
    
    def _generate_random_string(self, length:int = 10) -> None:
        return ''.join(sample(ascii_letters, length))
    
    def save(self) -> Memento:
        return ConcreteMemento(self._state)
    
    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        print(f'Originator: My state has changed to: {self._state}')
    
class Memento(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass

class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]
    
    def get_state(self) -> str:
        return self._state
    
    def get_date(self) -> str:
        return self._date

    def get_name(self) -> str:
        return f'{self._date} / ({self._state[0:9]})'

class Caretaker():
    """
    Care taker does not depend on Concrete Memento class. Therefore, it doesn't have 
    access to the originator's state, stored inside the memento. It works with all memento's via the
    base memento interface
    """

    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator
    
    def backup(self)-> None:
        print("Caretaker: Saving originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return
        memento = self._mementos.pop()
        print(f'Caretaker: Restoring state to: {memento.get_name()}')
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()
    
    def show_history(self) -> None:
        print("Caretaker: Here is the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())

if __name__ == "__main__":
    originator = Originator("Super duper")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print('Lets rollback. \n')
    caretaker.undo()

    print("Rollback once more. \n")
    caretaker.undo()