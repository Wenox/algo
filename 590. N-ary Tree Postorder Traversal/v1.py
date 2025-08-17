"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from typing import List


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        result = []

        def inner(root) -> None:
            if not root:
                return

            for child in root.children:
                inner(child)

            result.append(root.val)

        inner(root)

        return result
