class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)

        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1

            q = deque()
            visit = set()

            q.append([src, 1])
            visit.add(src)

            while q:
                ele, w = q.popleft()

                if ele == target:
                    return w

                for nei, weight in adj[ele]:
                    if nei not in visit:
                        q.append([nei, w * weight])
                        visit.add(nei)

            return -1
        
        res = []
        for query in queries:
            res.append(bfs(query[0], query[1]))
        return res


                




        # adj = collections.defaultdict(list)
        # for i, eq in enumerate(equations):
        #     a, b = eq
        #     adj[a].append([b, values[i]])
        #     adj[b].append([a, 1/values[i]])
        
        # def bfs(src, target):
        #     if src not in adj or target not in adj:
        #         return -1
        #     q = deque()
        #     visited = set()

        #     q.append([src, 1])
        #     visited.add(src)

        #     while q:
        #         n, w = q.popleft()
        #         if n == target:
        #             return w

        #         for nei, weight in adj[n]:
        #             if nei not in visited:
        #                 q.append([nei, w * weight])
        #                 visited.add(nei)
                
        #     return -1

        # res = []
        # for q in queries:
        #     res.append(bfs(q[0], q[1]))
        # return res
        