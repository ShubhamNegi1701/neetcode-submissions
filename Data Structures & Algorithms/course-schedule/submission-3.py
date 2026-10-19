class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            pre_map[course].append(prerequisite)

        visiting = set()

        def dfs(course):
            if course in visiting:
                return False

            if pre_map[course] == []:
                return True 
            
            visiting.add(course)

            for prereq in pre_map[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)

            # Mark this course as fully processed
            pre_map[course] = []
            
            return True

        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True