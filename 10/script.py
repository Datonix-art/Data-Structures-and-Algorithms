class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item): # push
        return self.items.insert(0, item)

    def dequeue(self): # pop
        if self.size() == 0:
            return None
        return self.items.pop()

    def peek(self):
        if self.size() == 0:
            return None
        return self.items[- 1]

    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue("Alice")
queue.enqueue("Bob")
queue.enqueue("Daniel")
queue.enqueue("John")

print(queue.peek())
print(queue.dequeue())
print(queue.size())

