# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBST(root, upperBound, lowerBound):
            if not root:
                return True
            if root.val <= lowerBound or root.val >= upperBound:
                return False
            return isBST(root.left, root.val, lowerBound) and isBST(root.right, upperBound, root.val)

        return isBST(root, float("inf"), float("-inf"))
        
        