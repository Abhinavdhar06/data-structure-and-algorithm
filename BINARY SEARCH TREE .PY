#PROGRAM TO  INSERT AN ELEMENT INTO BINARY SEARCH TREE

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def insert_into_bst(root, key):
    if not root:
        return TreeNode(key)

    if key < root.key:
        root.left = insert_into_bst(root.left, key)
    elif key > root.key:
        root.right = insert_into_bst(root.right, key)

    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)

# Example usage of insert_into_bst
bst_root = None

elements_to_insert = [50, 30, 70, 20, 40, 60, 80]

for element in elements_to_insert:
    bst_root = insert_into_bst(bst_root, element)

print("Binary Search Tree after insertion:")
inorder_traversal(bst_root)


#DELETE AN ELEMENT

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def insert_into_bst(root, key):
    if not root:
        return TreeNode(key)

    if key < root.key:
        root.left = insert_into_bst(root.left, key)
    elif key > root.key:
        root.right = insert_into_bst(root.right, key)

    return root

def delete_from_bst(root, key):
    if not root:
        return root

    if key < root.key:
        root.left = delete_from_bst(root.left, key)
    elif key > root.key:
        root.right = delete_from_bst(root.right, key)
    else:
        # Case 1: Node with only one child or no child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        # Case 2: Node with two children
        root.key = find_min_value(root.right).key
        root.right = delete_from_bst(root.right, root.key)

    return root

def find_min_value(node):
    while node.left:
        node = node.left
    return node

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)

# Example usage of delete_from_bst
bst_root = None

elements_to_insert = [50, 30, 70, 20, 40, 60, 80]

for element in elements_to_insert:
    bst_root = insert_into_bst(bst_root, element)

print("Binary Search Tree before deletion:")
inorder_traversal(bst_root)

element_to_delete = 30
bst_root = delete_from_bst(bst_root, element_to_delete)

print("\nBinary Search Tree after deletion of", element_to_delete, ":")
inorder_traversal(bst_root)

#SEARCH FOR KEY ELEMENTS

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def insert_into_bst(root, key):
    if not root:
        return TreeNode(key)

    if key < root.key:
        root.left = insert_into_bst(root.left, key)
    elif key > root.key:
        root.right = insert_into_bst(root.right, key)

    return root

def search_in_bst(root, key):
    if not root or root.key == key:
        return root

    if key < root.key:
        return search_in_bst(root.left, key)
    else:
        return search_in_bst(root.right, key)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)

# Example usage of search_in_bst
bst_root = None

elements_to_insert = [50, 30, 70, 20, 40, 60, 80]

for element in elements_to_insert:
    bst_root = insert_into_bst(bst_root, element)

print("Binary Search Tree:")
inorder_traversal(bst_root)

key_to_search = 40
search_result = search_in_bst(bst_root, key_to_search)

if search_result:
    print(f"\nKey {key_to_search} found in the Binary Search Tree.")
else:
    print(f"\nKey {key_to_search} not found in the Binary Search Tree.")
