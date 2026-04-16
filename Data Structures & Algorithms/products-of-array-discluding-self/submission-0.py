class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    

        #create the prefix array
        p = [1] * len(nums)

        #create the suffix array
        s = [1] * len(nums)

        r = [1] * len(nums)
        
        #build prefix array
        for i in range(1, len(nums)):
            p[i] = p[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            s[i] = s[i + 1] * nums[i + 1]
        
        for i in range(len(nums)):
            r[i] = p[i] * s[i]

        return r
