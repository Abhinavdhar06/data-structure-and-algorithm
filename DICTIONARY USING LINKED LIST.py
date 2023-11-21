class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedListDictionary:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        if not self.head:
            print("Dictionary is empty.")
            return

        if self.head.key == key:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current and current.key != key:
            prev = current
            current = current.next

        if not current:
            print("Key not found in the dictionary.")
            return

        prev.next = current.next

    def display(self):
        current = self.head
        while current:
            print(f"{current.key}: {current.value}", end=" -> ")
            current = current.next
        print("None")

# Example usage of LinkedListDictionary
dictionary = LinkedListDictionary()

dictionary.insert("name", "John")
dictionary.insert("age", 25)
dictionary.insert("city", "New York")

print("Dictionary:")
dictionary.display()

# Search operation
search_result = dictionary.search("age")
print("Search Result for 'age':", search_result)

# Delete operation
dictionary.delete("age")
print("Dictionary after deleting 'age':")
dictionary.display()
