# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def dfs(self, root):
    #     if not root:
    #         return
    #     return dfs(self, root.left) + dfs(self, root.right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            #diameter update
            self.diameter = max(self.diameter, left_height + right_height)

            #height
            return 1 + max(left_height, right_height)
        dfs(root)

        return self.diameter

        