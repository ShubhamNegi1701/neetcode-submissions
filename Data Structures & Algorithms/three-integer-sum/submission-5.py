class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1 
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1 
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
        # nums.sort()

        # for i, a in enumerate(nums):
        #     if a > 0:
        #         break 
        #     if i > 0 and a == nums[i - 1]:
        #         continue
        #     l, r = i + 1,len(nums) - 1

        #     while l < r:
        #         if nums[i] + nums[l] + nums[r] < 0:
        #             l += 1
        #         elif nums[i] + nums[l] + nums[r] > 0:
        #             r -= 1
        #         else:
        #             res.append([nums[i], nums[l], nums[r]])
        #             l += 1
        #             r -= 1
        #             while l < r and nums[l] == nums[l - 1]:
        #                 l += 1
        # return res