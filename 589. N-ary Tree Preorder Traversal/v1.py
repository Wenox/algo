# Revisit: 2 –– 16/08/2025

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from typing import List


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        result = []

        def inner(root: 'Node') -> None:
            if not root:
                return
            result.append(root.val)
            for child in root.children:
                inner(child)

        inner(root)

        return result


