# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        if not root:
            return []
        q.append(root)
        res = []

        while q:
            level = []
            for _ in range(len(q)):
                ele = q.popleft()
                level.append(ele)
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
            res.append(level[-1].val)

        return res

        