class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            #sorted array
            if nums[l] < nums[r]:
                # return nums[l]
                res = min(res, nums[l])
                break
            
            mid = (l + r) // 2
            res = min(res, nums[mid])
            
            # left sorted portion -> search right
            if nums[mid] >= nums[l]:
                l = mid + 1
            
            # right sorted portion -> search left
            else:
                r = mid - 1
        return res

