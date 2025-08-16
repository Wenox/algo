from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result, stack, curr = [], [], root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            popped = stack.pop()
            result.append(popped.val)
            curr = popped.right

        return result