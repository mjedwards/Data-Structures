class Node: 
    def __init__(self, value, next):
        self.value = value
        self.next = next # this is the next node in the list

class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.length = 0

    def __str__(self):
        pass
    
    def __len__(self): 
        return self.length
    
    def add_to_tail(self, value):
        if self.tail is None:
            new_tail = Node(value, None)

            self.head = new_tail
            self.tail = new_tail
        
        else:
            new_tail = Node(value, None)

            old_tail = self.tail
            old_tail.next = new_tail
            self.tail = new_tail
            
            self.length += 1

    def remove_head(self):
        if self.head is None:
            return None
        
        elif self.head == self.tail:
            current_head = self.head
            self.head = None

            self.tail = None

            self.length = self.length - 1

            return current_head.value
        
        else: 
            current_head = self.head
            self.head = current_head.next

            self.length = self.length - 1

            return current_head.value

    def remove_tail(self):
        if self.tail is None:
            return None

        if self.head == self.tail:
            current_tail = self.tail
            self.tail = None
            self.head = None
            self.length = self.length - 1
            return current_tail.value

        else:
            current_node = self.head

            while current_node.next != self.tail:
                current_node = current_node.next
            

            current_tail = self.tail
            self.tail = current_node

            current_node.next = None

            self.length = self.length - 1 
            return current_tail.value