class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        countS1 = Counter(s1)
        l = 0
        r = len(s1) - 1
        countS2 = Counter(s2[l:r+ 1])

        while r < len(s2):
            if countS1 == countS2:
                return True

            #remove l from countS2
            countS2[s2[l]] -= 1
            if countS2[s2[l]] == 0:
                del countS2[s2[l]]
            l += 1

            #remove r to countS2
            r += 1
            if r < len(s2):
                countS2[s2[r]] += 1

        return False