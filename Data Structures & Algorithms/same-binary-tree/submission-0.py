# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        sp = [p]
        sq = [q]

        while sp or sq:
            if len(sp) != len(sq):
                return False

            pp = sp.pop()
            qq = sq.pop()

            if not pp or not qq:
                if (pp and not qq) or (not pp and qq):
                    return False
                
                continue
            else:
                if pp.val != qq.val:
                    return False

            sp.append(pp.left)
            sq.append(qq.left)
            sp.append(pp.right)
            sq.append(qq.right)
        
        return True
        