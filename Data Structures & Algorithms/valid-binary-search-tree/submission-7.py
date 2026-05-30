# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bottom_check(self, root):
        root_min, root_max = root, root
        
        if root.left:
            left_min, left_max, correct = self.bottom_check(root.left)

            if not correct:
                return None, None, False
            
            if left_min and left_min.val >= root.val or left_max and left_max.val >= root.val:
                return None, None, False

            root_min = left_min
        
        if root.right:
            right_min, right_max, correct = self.bottom_check(root.right)

            if not correct:
                return None, None, False
            
            if right_min and right_min.val <= root.val or right_max and right_max.val <= root.val:
                return None, None, False
            
            root_max = right_max
        
        return root_min, root_max, True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.bottom_check(root)[2]