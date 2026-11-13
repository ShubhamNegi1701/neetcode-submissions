class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            prereqMap[crs].append(pre)

        visited = set()

        def dfs(crs):
            # course has no pre reqs so we can take it
            if prereqMap[crs] == []:
                return True

             # course has been visited, so we can take it
            if crs in visited:
                return True

            # visit the course in this exploration
            visited.add(crs)

            for preReq in prereqMap[crs]:
                if not dfs(preReq):
                    return False

            visited.remove(crs)

            prereqMap[crs] = []

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # preMap = { i:[] for i in range(numCourses)}

        # for crs, pre in prerequisites:
        #     preMap[crs].append(pre)

        # visitSet = set()

        # def dfs(crs):
        #     if crs in visitSet:
        #         return False
        #     if preMap[crs] == []:
        #         return True

        #     visitSet.add(crs)

        #     for pre in preMap[crs]:
        #         if not dfs(pre):
        #             return False

        #     visitSet.remove(crs)

        #     preMap[crs] = []

        #     return True
        
        # for i in range(numCourses):
        #     if not dfs(i):
        #         return False
        # return True
