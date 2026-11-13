class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        num_components = 0
        visited = set()

        adj = defaultdict(list)

        for source, sync in edges:
            adj[source].append(sync)
            adj[sync].append(source)

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nei in adj[node]:
                dfs(nei)
            
        for i in range(n):
            if i not in visited:
                num_components += 1
                dfs(i)

        return num_components

