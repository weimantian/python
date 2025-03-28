# 1. 定义树节点
class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 2. 创建平衡二叉树:
class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, value):

        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    # 递归插入
    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)
        
    # 中序遍历
    def inorder_traversal(self, node, visit):
        if node is not None:
            self.inorder_traversal(node.left, visit)
            visit(node.value)
            self.inorder_traversal(node.right, visit)

def print_value(value):
    print(value, end=' ')

# 创建二叉树
bt = BinaryTree()
elements = [7, 3, 9, 1, 4, 8, 10]
for el in elements:
    bt.insert(el)

bt.inorder_traversal(bt.root, print_value)
        
