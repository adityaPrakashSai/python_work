import queue

class ObjectPool:
    def __init__(self, queue, auto_get = False) -> None:
        self._queue = queue
        self.item = self._queue.get() if auto_get else None
    
    def __enter__(self):
        if self.item is None:
            self.item = self._queue.get()
        return self.item
    
    def __exit__(self, Type, value, traceback):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None
    
    def __del__(self):
        if self.item is not None:
            self._queue.put(self.item)
            self.item = None

def main():
    sample_queue = queue.Queue()
    sample_queue.put('lily')
    sample_queue.put('rose')
    with ObjectPool(sample_queue) as obj:
        print('Inside with: {}'.format(obj))

if __name__ == "__main__":
    main()
