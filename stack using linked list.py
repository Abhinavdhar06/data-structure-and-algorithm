class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack underflow. Cannot pop from an empty stack.")
            return None
        else:
            popped_item = self.top.data
            self.top = self.top.next
            return popped_item

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        else:
            return self.top.data

# Example usage of Stack using Linked List
stack_linked_list = StackLinkedList()
stack_linked_list.push(1)
stack_linked_list.push(2)
stack_linked_list.push(3)

print("\nStack using Linked List:")
print("Peek:", stack_linked_list.peek())  # Should print 3
print("Pop:", stack_linked_list.pop())    # Should print 3
print("Pop:", stack_linked_list.pop())    # Should print 2
print("Is empty:", stack_linked_list.is_empty())  # Should print False
