#creation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

def create_linked_list():
    linked_list = LinkedList()
    n = int(input("Enter the number of elements in the linked list: "))
    for _ in range(n):
        element = int(input("Enter element: "))
        linked_list.append(element)
    return linked_list

if __name__ == "__main__":
    my_linked_list = create_linked_list()
    print("Linked List:")
    my_linked_list.display()

#insertion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                print("Position out of bounds")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

def create_linked_list():
    linked_list = LinkedList()
    n = int(input("Enter the number of elements in the linked list: "))
    for _ in range(n):
        element = int(input("Enter element: "))
        linked_list.append(element)
    return linked_list

if __name__ == "__main__":
    my_linked_list = create_linked_list()
    print("Linked List:")
    my_linked_list.display()

    # Example of insertion at a specific position
    data_to_insert = int(input("Enter the data to insert: "))
    position_to_insert = int(input("Enter the position to insert: "))
    my_linked_list.insert(data_to_insert, position_to_insert)

    print("Linked List after insertion:")
    my_linked_list.display()

#deletion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                print("Position out of bounds")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, position):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        if position == 0:
            self.head = self.head.next
            return

        current = self.head
        for _ in range(position - 1):
            if current.next is None:
                print("Position out of bounds")
                return
            current = current.next

        if current.next is None:
            print("Position out of bounds")
            return

        current.next = current.next.next

def create_linked_list():
    linked_list = LinkedList()
    n = int(input("Enter the number of elements in the linked list: "))
    for _ in range(n):
        element = int(input("Enter element: "))
        linked_list.append(element)
    return linked_list

if __name__ == "__main__":
    my_linked_list = create_linked_list()
    print("Linked List:")
    my_linked_list.display()

    # Example of deletion at a specific position
    position_to_delete = int(input("Enter the position to delete: "))
    my_linked_list.delete(position_to_delete)

    print("Linked List after deletion:")
    my_linked_list.display()

#traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                print("Position out of bounds")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, position):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        if position == 0:
            self.head = self.head.next
            return

        current = self.head
        for _ in range(position - 1):
            if current.next is None:
                print("Position out of bounds")
                return
            current = current.next

        if current.next is None:
            print("Position out of bounds")
            return

        current.next = current.next.next

    def traverse(self):
        current = self.head
        while current:
            # Perform some operation on the data (printing in this case)
            print(current.data, end=" ")
            current = current.next

def create_linked_list():
    linked_list = LinkedList()
    n = int(input("Enter the number of elements in the linked list: "))
    for _ in range(n):
        element = int(input("Enter element: "))
        linked_list.append(element)
    return linked_list

if __name__ == "__main__":
    my_linked_list = create_linked_list()
    print("Linked List:")
    my_linked_list.display()

    # Example of traversal
    print("Traversing the Linked List:")
    my_linked_list.traverse()

