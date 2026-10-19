# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        stack = [(root, root.val)]
        
        while stack:
            curr, maxSoFar = stack.pop()
            if curr.val >= maxSoFar:
                res += 1
            maxSoFar = max(maxSoFar, curr.val)
            if curr.left:
                stack.append((curr.left, maxSoFar))
            if curr.right:
                stack.append((curr.right, maxSoFar))
        
        return res

