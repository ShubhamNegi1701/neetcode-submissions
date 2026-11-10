class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        countS1 = Counter(s1)
        l = 0
        r = len(s1) - 1

        while r < len(s2):
            countS2 = Counter(s2[l:r+ 1])
            if countS1 == countS2:
                return True
            else:
                r += 1
                l += 1

        return False