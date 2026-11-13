class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqMap = { i:[] for i in range(numCourses) }

        for crs, pre in prerequisites:
            prereqMap[crs].append(pre)

        visited = set()
        visiting = set()
        output = []

        def dfs(crs):
            if crs in visited:
                return True
            if crs in visiting:
                return False

            visiting.add(crs)

            for pre in prereqMap[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)

            visited.add(crs)

            output.append(crs)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return output

        
