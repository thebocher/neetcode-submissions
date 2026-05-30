# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(node):
            if node is None:
                return

            heapq.heappush(arr, node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        for _ in range(k-1):
            heapq.heappop(arr)

        return heapq.heappop(arr)        