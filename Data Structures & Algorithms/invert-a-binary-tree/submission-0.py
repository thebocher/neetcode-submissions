# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, t: Optional[TreeNode]) -> Optional[TreeNode]:
        if t is None:
            return None

        t.left, t.right = t.right, t.left

        if t.left:
            self.invertTree(t.left)
        
        if t.right:
            self.invertTree(t.right)
        
        return t
        