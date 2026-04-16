"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            #create copy
            copy = Node(node.val)

            #add copy to the oldToNew list
            oldToNew[node] = copy
            
            #obtain all its neighbors
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            #return to the caller
            return copy
        
        return dfs(node) if node else None