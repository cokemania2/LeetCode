# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_value = 0

    def _find_max_length(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return 0
        answer = []
        left = 0
        right = 0
        if root.left is not None:
            left = self._find_max_length(root.left) + 1
        if root.right is not None:
            right = self._find_max_length(root.right) + 1
        if left + right > self.max_value:
            self.max_value = left + right
        return max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self._find_max_length(root)
        return self.max_value