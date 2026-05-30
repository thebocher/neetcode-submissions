# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # pre: 1 2 4 5 3 6 7
        # in:  4 2 5 1 6 3 7
        if not len(inorder):
            return None

        head = TreeNode(preorder[0])
        left_inorder = inorder[ :inorder.index(preorder[0]) ]
        right_inorder = inorder[ inorder.index(preorder[0])+1: ]

        del preorder[0]

        head.left = self.buildTree(preorder, left_inorder)
        head.right = self.buildTree(preorder, right_inorder)

        return head




        