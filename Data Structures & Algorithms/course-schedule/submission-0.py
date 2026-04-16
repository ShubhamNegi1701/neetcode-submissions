class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course with its pre-requisites
        prereqMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereqMap[crs].append(pre)
        
        # Store all courses along the current DFS path
        visiting = set()

        # Check if every course can be scheduled
        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False
            if prereqMap[crs] == []:
                # No pre-req for the course, can take
                return True

            # Add course in visiting set
            visiting.add(crs)

            for pre in prereqMap[crs]:
                if not dfs(pre):
                    return False
            
            # All pre-reqs for the course are met
            visiting.remove(crs)
            prereqMap[crs] = []
            return True
        
        # There can be disjointed graphs. Calling DFS for all courses.
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        # All courses can be finished
        return True




