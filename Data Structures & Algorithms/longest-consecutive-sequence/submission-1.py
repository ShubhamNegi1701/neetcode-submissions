class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            numSet.add(num)
        
        res = 0
        for num in numSet:
            count = 1
            if (num - 1) in numSet:
                continue
            else:
                #starting point
                nextNum = num + 1
                while nextNum in numSet:
                    count += 1
                    nextNum += 1

                res = max(res, count)
        return res
