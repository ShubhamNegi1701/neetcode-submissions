# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()

        if root:
            q.append(root)
        else:
            return []

        while q:
            level = []
            level_size = len(q)
            for i in range(level_size):
                ele = q.popleft()

                if i == level_size - 1:
                    res.append(ele.val)

                if ele.left:
                    q.append(ele.left)
                
                if ele.right:
                    q.append(ele.right)

        return res
        
