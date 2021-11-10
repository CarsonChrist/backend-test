# Node class for LinkedList
class Node:
    
    def __init__(self, value = None):
        self.value = value
        self.next = None
# LinkedList class to contain transactions implemented in point_tracker.py
class LinkedList:

    # Default constructor
    def __init__(self):
        self.head = None

    # Append a new node to the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)     
        if self.head is None:
            self.head = new_node
        else:
            last_value = self.head
            while last_value.next is not None:
                last_value = last_value.next
            last_value.next = new_node

    # Insert a new node into the linked list that maintains sort
    def insert(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            new_node.next = None
        elif new_value < self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            pointer1 = self.head
            pointer2 = self.head.next
            while pointer2 is not None:
                if new_value < pointer2.value:
                    new_node.next = pointer2
                    pointer1.next = new_node
                    return
                pointer1 = pointer1.next
                pointer2 = pointer2.next
            pointer1.next = new_node

    # Return Linked list head
    def get_head(self):
        return self.head

    # Yield each node of the Linked list
    def iterate(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    # Remove the head from the Linked list
    def remove_head(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next
            return