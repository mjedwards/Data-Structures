"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
       
        if self.head is None:
       
            new_node = ListNode(value, None)
       
            self.head = new_node
       
            self.tail = new_node
      
            self.length += 1
        else:
       
            new_node = ListNode(value, self.head)
       
            self.head = new_node
      
            self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
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
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.tail is None:
            new_tail = ListNode(value, None)

            self.head = new_tail
            self.tail = new_tail
        
        else:
            new_tail = ListNode(value, None)

            old_tail = self.tail
            old_tail.next = new_tail
            self.tail = new_tail 
            
            self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
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
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # Remove at index i:
        # 0) Check that length > i. If not, return None
        if node >= self.length:
            return None
        if self.length == 1 and node == 0:
            target = self.head
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return target.value
        # Iterate through the loop i-1 times:
        prev_node = self.head
        for i in range(node - 1):
        # This will get us to prev_node points to the node before the target node
            prev_node = prev_node.next
        target = prev_node.next
        prev_node.next = target.next
        target.next = None
        self.length = self.length - 1
        return target.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
          
        if self.length == 0:
            return None
        
        if self.length == 1:
            return self.head.value
        
        current_max = self.head.value
        
        current_node = self.head
       
        while current_node is not None:
        
            if current_max < current_node.value:
                current_max = current_node.value
       
            current_node = current_node.next
       
        return current_max