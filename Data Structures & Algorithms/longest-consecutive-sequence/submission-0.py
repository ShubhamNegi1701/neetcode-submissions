class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #first store if an element was found in a hashmap
        map = {}
        for n in nums:
            if n not in map:
                map[n] = 1
        #find the starting points of each sequence
        starts = []
        for n in map:
            if n-1 not in map:
                starts.append(n)
        
        #count how many elements u can get from that start point and store the max and return it
        longestLength = 0
        for s in starts:
            currLength = 1 
            while s+1 in map:
                currLength +=1
                s+=1
            longestLength = max(longestLength, currLength)
               
                
        return longestLength


