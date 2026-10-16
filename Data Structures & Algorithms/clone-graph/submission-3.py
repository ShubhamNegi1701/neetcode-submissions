"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeToCopy = {}
        def clone(node):
            if node is None:
                return None
                
            if node in nodeToCopy:
                return nodeToCopy[node]
            
            copy_node = Node(node.val)
            nodeToCopy[node] = copy_node

            for nei in node.neighbors:
                copy_node.neighbors.append(clone(nei))
            return nodeToCopy[node]
        
        return clone(node)


