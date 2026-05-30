# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treesEqual(self, tree1, tree2):
        if (tree1 is None and tree2 is not None) or (tree1 is not None and tree2 is None):
            return False
        elif tree1 is None and tree2 is None:
            return True

        if tree1.val != tree2.val:
            return False
        
        return (
            self.treesEqual(tree1.left, tree2.left) 
                and self.treesEqual(tree1.right, tree2.right)
        )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None or subRoot is None:
            return False

        if root.val != subRoot.val:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        return (
            self.treesEqual(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )