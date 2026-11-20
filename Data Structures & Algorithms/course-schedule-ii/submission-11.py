class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] += 1

        q = deque()

        # add courses with no pre-requisites
        q = deque(i for i in range(numCourses) if indegree[i] == 0)


        order = []

        while q:
            node = q.popleft()
            order.append(node)
            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        return order if len(order) -- numCourses else []

        
