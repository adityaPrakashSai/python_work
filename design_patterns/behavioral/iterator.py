# collections are one of the most used data types in programming
# No matter how a collection is structured, it must provide a way of 
# accessing its elements so that other code can use these elements
# there should be a way to go over all the elements without accessing these elements again

from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

"""
to create an iterator in python, there are two abstract classes from the built-in collections
module - Iterable and Iterator. We need to implement the '__iter__()' method in the iterated object
(collection), and the '__next__()' method in the iterator
"""

class AlphabeticalOrderIterator(Iterator):
    """
    Concrete iterators implement various traversal algorithms. these classes
    store the current traversal position at all times. 
    """

    """
    _position attribute stores the current traversal position. 
    An iterator may have a lot of other fields for storing iteration state,
    especially when it is supposed to work with a particular kind of collection
    """

    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = - 1 if reverse else 0
    
    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value

class WordsCollection(Iterable):
    """
    Concrete collections provide one or several methods for retrieving fresh
    iterator instances, compatible with the collection class
    """

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection
    
    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)
    
    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)
    
    def add_item(self, item: Any):
        self._collection.append(item)
    
def main():
    collections = WordsCollection()
    collections.add_item("First")
    collections.add_item("Second")
    collections.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collections))
    print("")
    print("Reverse Traversal: ")
    print("\n".join(collections.get_reverse_iterator()), end="")

if __name__ == "__main__":
    main()