from math import log, floor

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def fillRes(self, root, level, res):
        if len(res)-1 < level:
            res.append([])
        
        res[level].append(root.val)

        if root.left:
            self.fillRes(root.left, level+1, res)
        
        if root.right:
            self.fillRes(root.right, level+1, res)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if root is None:
            return []

        self.fillRes(root, 0, res)
        return res