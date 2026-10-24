class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0] * 26
        s2_freq = [0] * 26

        if len(s1) > len(s2):
            return False

        for s in s1:
            s1_freq[ord(s) - ord('a')] += 1
        
        l = 0
        r = len(s1) - 1

        for i in range(len(s1)):
            s2_freq[ord(s2[i]) - ord('a')] += 1


        while r < len(s2):
            if s1_freq == s2_freq:
                return True
            
            s2_freq[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1

            if r < len(s2):
                index = ord(s2[r]) - ord('a')
                s2_freq[index] += 1
                
        return False
