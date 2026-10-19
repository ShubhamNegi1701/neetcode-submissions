class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = { c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visited = set()
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True

            visiting.add(crs)

            for pre in prereq[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            visited.add(crs)
            output.append(crs)

            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output


