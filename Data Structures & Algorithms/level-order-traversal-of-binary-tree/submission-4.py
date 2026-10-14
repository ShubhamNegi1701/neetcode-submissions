# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()

        if root:
            q.append(root)
        else:
            return []

        while q:
            level = []
            for _ in range(len(q)):
                ele = q.popleft()
                level.append(ele.val)

                if ele.left:
                    q.append(ele.left)
                
                if ele.right:
                    q.append(ele.right)


            res.append(level)

        return res
