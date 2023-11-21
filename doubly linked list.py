class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
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
        new_node.prev = last

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                print("Position out of bounds")
                return
            current = current.next
        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        new_node.prev = current
        current.next = new_node

    def delete(self, position):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        if position == 0:
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
            return

        current = self.head
        for _ in range(position):
            if current is None:
                print("Position out of bounds")
                return
            current = current.next

        if current is None:
            print("Position out of bounds")
            return

        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

def create_doubly_linked_list():
    linked_list = DoublyLinkedList()
    n = int(input("Enter the number of elements in the linked list: "))
    for _ in range(n):
        element = int(input("Enter element: "))
        linked_list.append(element)
    return linked_list

if __name__ == "__main__":
    my_linked_list = create_doubly_linked_list()
    print("Doubly Linked List:")
    my_linked_list.display()

    # Example of insertion at a specific position
    data_to_insert = int(input("Enter the data to insert: "))
    position_to_insert = int(input("Enter the position to insert: "))
    my_linked_list.insert(data_to_insert, position_to_insert)

    print("Doubly Linked List after insertion:")
    my_linked_list.display()

    # Example of deletion at a specific position
    position_to_delete = int(input("Enter the position to delete: "))
    my_linked_list.delete(position_to_delete)

    print("Doubly Linked List after deletion:")
    my_linked_list.display()

    # Example of traversal
    print("Traversing the Doubly Linked List:")
    my_linked_list.traverse()
