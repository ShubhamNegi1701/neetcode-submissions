class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = defaultdict(list)

        if len(edges) != n-1:
            return False

        visited = set()

        for src, sync in edges:
            adj[src].append(sync)
            adj[sync].append(src)

        def dfs(num):
            if num in visited:
                return 
            
            visited.add(num)

            for nei in adj[num]:
                dfs(nei)

        dfs(0)

        return len(visited) == n

        
































        # adj = defaultdict(list)

        # if len(edges) != n - 1:
        #     return False 

        # for source, sync in edges:
        #     adj[source].append(sync)
        #     adj[sync].append(source)

        # visited = set()

        # def dfs(node):
        #     if node in visited:
        #         return

        #     visited.add(node)

        #     for nei in adj[node]:
        #         dfs(nei)

        # dfs(0)

        # return len(visited) == n


            
            
