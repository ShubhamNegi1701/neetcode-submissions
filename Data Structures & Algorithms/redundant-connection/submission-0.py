class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        def dfs(src, target, visited):
            if src in visited:
                return False

            if src == target:
                return True

            visited.add(src)

            for nei in adj[src]:
                if dfs(nei, target, visited):
                    return True
            
            return False


        for edge in edges:
            visited = set()
            src, sync = edge
            if not dfs(src, sync, visited):
                adj[src].append(sync)
                adj[sync].append(src)
            else:
                return edge