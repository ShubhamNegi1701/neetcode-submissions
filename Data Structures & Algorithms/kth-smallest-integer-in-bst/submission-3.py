# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = None

        def dfs(curr):
            nonlocal k, result

            if curr is None or result is not None:
                return 

            dfs(curr.left)

            k -= 1
            if k == 0:
                result = curr.val
                return

            dfs(curr.right)
        
        dfs(root)
        return result
