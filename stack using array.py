class StackArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def push(self, item):
        if self.is_full():
            print("Stack overflow. Cannot push item:", item)
        else:
            self.stack[self.size] = item
            self.size += 1

    def pop(self):
        if self.is_empty():
            print("Stack underflow. Cannot pop from an empty stack.")
            return None
        else:
            popped_item = self.stack[self.size - 1]
            self.size -= 1
            return popped_item

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        else:
            return self.stack[self.size - 1]

# Example usage of Stack using Array
stack_array = StackArray(5)
stack_array.push(1)
stack_array.push(2)
stack_array.push(3)

print("Stack using Array:")
print("Peek:", stack_array.peek())  # Should print 3
print("Pop:", stack_array.pop())    # Should print 3
print("Pop:", stack_array.pop())    # Should print 2
print("Is empty:", stack_array.is_empty())  # Should print False
print("Is full:", stack_array.is_full())    # Should print False
