"""
*What is this pattern about ?
This patterns aims to redice the number of classes required by an application. 
Instead of relying on subclasses it creates objects by copying a prototypical instance at run-time.

This is useful as it makes it easier to derive new kinds of objects, when instances of the classe have only a few different 
combinations of state, and when instantiation is expensive.

* What does this example do ?
When the number of prototypes in an application can vary, it can be useful to 
keep a dispatcher. This allows clients to query the dispatcher for a prototype before cloning 
a new instance

Below provides an example of such dispatcher, which contains 3 copies of prototype: 'default', 'objecta' and 'objectb'
creates a new object instance by cloning prototype
"""

from __future__ import annotations
from typing import Any
import copy

class Prototype:
    def __init__(self, value: str = 'default', **attrs: Any) -> None:
        self.value = value
        self.__dict__.update(attrs)
    
    def clone(self, **attrs: Any) -> Prototype:
        cloned_object = copy.deepcopy(self)
        cloned_object.__dict__.update(attrs)
        return cloned_object

class PrototypeDispatcher:
    def __init__(self):
        self._objects = {}
    
    def get_objects(self) -> dict[str, Prototype]:
        return self._objects
    
    def register_object(self, name: str, obj: Prototype) -> None:
        self._objects[name] = obj
    
    def unregister_object(self, name: str) -> None:
        del self._objects[name]
    

def main()-> None:
    dispatcher = PrototypeDispatcher()
    prototype = Prototype()
    d = prototype.clone()
    a = prototype.clone(value='a-value', category = 'a')
    b = a.clone(value='b-value', is_checked = True)
    dispatcher.register_object('objecta', a)
    dispatcher.register_object('objectb', b)
    dispatcher.register_object('default', d)

    print([{n : p.value} for n, p in dispatcher.get_objects().items()])

if __name__ == "__main__":
    main()
    
