# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        start_counting = False

        def dfs(node):
            nonlocal start_counting, k
            if node.left:
                result = dfs(node.left)

                if result is not None:
                    return result
            else:
                if start_counting == False:
                    start_counting = True
            
            if start_counting:
                k -= 1

            if k == 0:
                return node.val

            if node.right:
                result = dfs(node.right)

                if result is not None:
                    return result
            


        return dfs(root)
        