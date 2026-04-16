class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create a hashmap 
        map = {}
        #iterate thru list and add elements to hashmap if not found in the list
        for n in nums:
            if n in map:
                return True
            else:
                map[n] = 1
        return False
        #if found in the list return true 
        #return false