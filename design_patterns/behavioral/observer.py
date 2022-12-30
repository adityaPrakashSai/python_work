# publisher - subscriber pattern

from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Subject(ABC):
    """
    the subject interface declares a set of methods for managing 
    subscribers
    """
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        '''
        Attach an observer to the subject
        '''
        pass
    
    @abstractmethod
    def detach(self, observer: Observer) -> None:
        '''
        Detach an observer from the subject
        '''
        pass
    
    @abstractmethod
    def notify(self) -> None:
        '''
        Notify all observers about an event
        '''
        pass

class ConcreteSubject(Subject):
    """
    the subject owns some important state and notifies observers when the state changes
    """

    _state : int = None

    _observers: List[Observer] = []
    """
    list of subscribers. in real life, the list of subscribers can be stored more comprehensively.
    """

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)
    
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
    
    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)
    
    def some_business_logic(self):
        self._state = randrange(0, 10)
        print(f'Subject: My state has changed to: {self._state}')
        self.notify()

class Observer(ABC):
    """
    the observer interface declares the update method, used by subjects
    """
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")

class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")

def main():
    subject = ConcreteSubject()
    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()
    subject.attach(observer_a)
    subject.attach(observer_b)
    subject.some_business_logic()
    subject.some_business_logic()
    subject.detach(observer_a)
    subject.some_business_logic()


if __name__ == "__main__":
    main()
