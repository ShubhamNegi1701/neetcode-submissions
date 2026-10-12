class Solution:
    def isElementFound(self, numbers: List[int], startingIdx: int, endingIndex:int, target: int) -> int:
        s, e = startingIdx, endingIndex
        while s <= e:
            m = (s + e) // 2
            if numbers[m] < target:
                s = m + 1
            elif numbers[m] > target:
                e = m - 1
            else:
                return m
        return -1
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                t = - nums[i] - nums[j]
                k = self.isElementFound(nums, j + 1, len(nums) - 1, t)
                if k != -1:
                    res.append([nums[i], nums[j], nums[k]])
        return res




