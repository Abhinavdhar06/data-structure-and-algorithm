class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow. Cannot dequeue from an empty queue.")
            return None
        else:
            dequeued_item = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return dequeued_item

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        else:
            return self.front.data

# Example usage of Queue using Linked List
queue_linked_list = QueueLinkedList()
queue_linked_list.enqueue(1)
queue_linked_list.enqueue(2)
queue_linked_list.enqueue(3)

print("\nQueue using Linked List:")
print("Peek:", queue_linked_list.peek())  # Should print 1
print("Dequeue:", queue_linked_list.dequeue())  # Should print 1
print("Dequeue:", queue_linked_list.dequeue())  # Should print 2
print("Is empty:", queue_linked_list.is_empty())  # Should print False
