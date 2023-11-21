class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.key, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.key, end=" ")

# Example usage of tree traversal methods
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder Traversal:")
inorder_traversal(root)
print("\n\nPreorder Traversal:")
preorder_traversal(root)
print("\n\nPostorder Traversal:")
postorder_traversal(root)
