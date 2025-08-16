# Revisit: 2 –– 16/08/2025
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []

        def helper(root):
            if not root:
                return

            vals.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        return vals