class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bag = float("-inf")
        max_sub = float("-inf")

        for n in nums:
            if bag < 0:
                bag = n
            else:
                bag += n
            max_sub = max(bag, max_sub)
        return max_sub


