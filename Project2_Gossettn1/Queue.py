# Implementation of the queue data structure.
# A list is used to store queue elements, where the tail 
# of the queue is element 0, and the head is
# the last element

class Queue:
    '''
    Constructor.  Initializes the list items
    '''
    def __init__(self):
        self.items = []
    
    '''
    Returns true if queue is empty, false otherwise
    '''
    def is_empty(self):
        return self.items == []
    
    '''
    Enqueue: Add item to end (tail) of the queue
    '''
    def enqueue(self, item):
        self.items.insert(0,item)
        
    '''
    Dequeue: Remove item from font of the queue
    '''
    def dequeue(self):
        return self.items.pop()
    
    '''
    Returns queue size
    '''
    def size(self):
        return len(self.items)
    
def main():
    # Illustrates FIFO behavior
    q = Queue()
    q.enqueue('hello')
    q.enqueue('dog')
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print("Queue size: ", q.size())
    
    
if __name__ == '__main__':
    main()