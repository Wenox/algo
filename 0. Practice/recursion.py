import random


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generate_random_tree(depth: int, branch_probability: float):
    if depth == 0 or random.random() > branch_probability:
        return None

    node = TreeNode(random.randint(1, 99))
    node.left = generate_random_tree(depth - 1, branch_probability)
    node.right = generate_random_tree(depth - 1, branch_probability)
    return node


def print_tree(root: TreeNode):
    if not root:
        return

    print(f"Node: {root.val}")
    print_tree(root.left)
    print_tree(root.right)


def preorder_to_string(root):
    values = []

    def dfs(node):
        if not node:
            return
        values.append(str(node.val))  # N: process current node
        dfs(node.left)                # L
        dfs(node.right)               # R

    dfs(root)
    return ", ".join(values)



root = generate_random_tree(6, branch_probability=0.9)
print_tree(root)
print(preorder_to_string(root))
