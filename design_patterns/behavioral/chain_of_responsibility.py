
"""
this pattern aims to decouple the senders of a request 
from its receivers by allowing requests to move through chained receivers
until it is handled
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):
    """
    Declares a method for building a chain of handlers.
    It also declares a method for executing a request
    """
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass

class AbstractHandler(Handler):
    """
    The default chaining behavior
    """
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler
    
    def handle(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        
        return None

class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> Optional[str]:
        if request == 'Banana':
            return f'Monkey: I will eat the {request}'
        else:
            return super().handle(request)

class SquirrelHandler(AbstractHandler):
    def handle(self, request):
        if request == 'Nut':
            return f'Squirrel: I will eat the {request}'
        else:
            super().handle(request)

class DogHandler(AbstractHandler):
    def handle(self, request):
        if request == 'MeatBall':
            return f'Dog: I will eat the request'
        else:
            return super().handle(request)

def client_code(handler: Handler):
    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f'\n Client: Who wants {food} ?')
        result = handler.handle(food)
        if result:
            print(f'{result}', end="")
        else:
            print(f'{food} was left untouched.', end="")

def main():
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()
    monkey.set_next(squirrel).set_next(dog)
    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print("\n")
    print("Subchain: squirrel > dog")
    client_code(squirrel)


if __name__ == "__main__":
    main()