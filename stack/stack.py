"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

import time
from singly_linked_list import LinkedList

class Stack_One:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
        self.next = None

    

    def __len__(self):
        return self.storage.length

    def push(self, value):
        return self.storage.add_to_tail()

    def pop(self):
        return self.storage.remove_tail()

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) == 0:
            return None
        return self.storage.pop()



n = 100000
stack = Stack()
start = time.time()
for i in range(n):
    stack.push(i)
print("Pushing (to front): ", time.time() - start)
start = time.time()
for i in range(n):
    stack.pop()
print("Popping (from front): ", time.time() - start)

stack_one = Stack_One()

for i in range(n):
    stack_one.storage.add_to_tail(i)
print("Adding (to tail): ", time.time() - start)
start = time.time()

for i in range(n):
    stack_one.storage.remove_head()
print("Removing (from head): ", time.time() - start)