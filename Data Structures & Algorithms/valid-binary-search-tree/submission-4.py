# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validBST(curr, lowerBound, upperBound):
            if not curr: 
                return True

            return lowerBound < curr.val and upperBound > curr.val and validBST(curr.left, lowerBound, curr.val) and validBST(curr.right, curr.val, upperBound)

        return validBST(root, float("-inf"), float("inf"))