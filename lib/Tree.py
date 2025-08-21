class BinaryTree: # or BinarySearchTree
    
    def __init__(self):
        self.root = None


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

#Simple tree(non-binary) structure
class Tree:
    def __init__(self):
        self.root = None

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []  # List to hold children nodes