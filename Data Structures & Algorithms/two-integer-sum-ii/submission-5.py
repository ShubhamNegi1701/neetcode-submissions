class Solution:
    def isElementFound(self, numbers: List[int], startingIdx: int, target: int) -> int:
        s, e = startingIdx, len(numbers) - 1
        while s <= e:
            m = (s + e) // 2
            if numbers[m] < target:
                s = m + 1
            elif numbers[m] > target:
                e = m - 1
            else:
                return m
        return -1


    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            complement = target - num
            foundIdx = self.isElementFound(numbers, i + 1, complement)
            if foundIdx != -1:
                return [i + 1, foundIdx + 1]
        return []