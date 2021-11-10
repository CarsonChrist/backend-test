class Node:
    
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def appendFront(self, new_value):       
        new_node = Node(new_value) 
        new_node.next = self.head
        self.head = new_node

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            last_value = self.head
            while last_value.next is not None:
                last_value = last_value.next
            last_value.next = new_node

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

    def get_head(self):
        return self.head

    def iterate(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def list(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def remove_head(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next
            return

    # remove node
    def remove(self, key):
        if self.head is None:
            return
        if key == self.head.value:
            self.head = self.head.next
            return
        pointer1 = self.head
        pointer2 = self.head.next
        while pointer2 is not None:
            if key == pointer2.value:
                pointer1.next = pointer2.next
                pointer2 = None
                return
            pointer1 = pointer1.next
            pointer2 = pointer2.next

