class QueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue overflow. Cannot enqueue item:", item)
        else:
            if self.is_empty():
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow. Cannot dequeue from an empty queue.")
            return None
        else:
            dequeued_item = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.capacity
            return dequeued_item

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        else:
            return self.queue[self.front]

# Example usage of Queue using Array
queue_array = QueueArray(5)
queue_array.enqueue(1)
queue_array.enqueue(2)
queue_array.enqueue(3)

print("Queue using Array:")
print("Peek:", queue_array.peek())  # Should print 1
print("Dequeue:", queue_array.dequeue())  # Should print 1
print("Dequeue:", queue_array.dequeue())  # Should print 2
print("Is empty:", queue_array.is_empty())  # Should print False
print("Is full:", queue_array.is_full())    # Should print False
