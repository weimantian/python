class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        else:  # value >= node.value
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)

    def inorder_traversal(self, node, visit):
        if node is not None:
            self.inorder_traversal(node.left, visit)
            visit(node.value)
            self.inorder_traversal(node.right, visit)

    def preorder_traversal(self, node, visit):
        if node is not None:
            visit(node.value)
            self.preorder_traversal(node.left, visit)
            self.preorder_traversal(node.right, visit)

    def postorder_traversal(self, node, visit):
        if node is not None:
            self.postorder_traversal(node.left, visit)
            self.postorder_traversal(node.right, visit)
            visit(node.value)

def print_value(value):
    print(value, end=' ')

# 创建二叉树
bt = BinaryTree()
elements = [7, 3, 9, 1, 4, 8, 10]
for el in elements:
    bt.insert(el)

# 中序遍历
print("Inorder Traversal:")
bt.inorder_traversal(bt.root, print_value)
print()

# 前序遍历
print("Preorder Traversal:")
bt.preorder_traversal(bt.root, print_value)
print()

# 后序遍历
print("Postorder Traversal:")
bt.postorder_traversal(bt.root, print_value)
print()