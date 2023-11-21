class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if not self.head:
            print("Circular Linked List is empty.")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print()

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        last = self.head
        while last.next != self.head:
            last = last.next

        last.next = new_node
        new_node.next = self.head

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = new_node
            self.head = new_node
            return

        current = self.head
        for _ in range(position - 1):
            if current.next == self.head:
                print("Position out of bounds")
                return
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def delete(self, key):
        if not self.head:
            print("Circular Linked List is empty.")
            return

        if self.head.data == key:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            return

        current = self.head
        prev = None
        while current.next != self.head:
            prev = current
            current = current.next
            if current.data == key:
                prev.next = current.next
                return

        print(f"Key {key} not found in the Circular Linked List.")

    def traverse(self):
        if not self.head:
            print("Circular Linked List is empty.")
            return

        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break

def create_circular_linked_list():
    linked_list = CircularLinkedList()
    n = int(input("Enter the number of elements in the linked list: "))
    for _ in range(n):
        element = int(input("Enter element: "))
        linked_list.append(element)
    return linked_list

if __name__ == "__main__":
    my_linked_list = create_circular_linked_list()
    print("Circular Linked List:")
    my_linked_list.display()

    # Example of insertion at a specific position
    data_to_insert = int(input("Enter the data to insert: "))
    position_to_insert = int(input("Enter the position to insert: "))
    my_linked_list.insert(data_to_insert, position_to_insert)

    print("Circular Linked List after insertion:")
    my_linked_list.display()

    # Example of deletion
    key_to_delete = int(input("Enter the key to delete: "))
    my_linked_list.delete(key_to_delete)

    print("Circular Linked List after deletion:")
    my_linked_list.display()

    # Example of traversal
    print("Traversing the Circular Linked List:")
    my_linked_list.traverse()
