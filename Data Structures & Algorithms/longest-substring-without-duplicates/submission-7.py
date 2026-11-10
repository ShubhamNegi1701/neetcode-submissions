class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        dupes = set()
        maxSoFar = 0
        while r < len(s):
            curr = 0
            if s[r] not in dupes:
                dupes.add(s[r])
                r += 1
            else:
                while s[r] in dupes:
                    dupes.remove(s[l])
                    l += 1
            curr = r - l 
            maxSoFar = max(maxSoFar, curr)

        return maxSoFar

             