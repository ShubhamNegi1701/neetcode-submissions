class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapStoT, mapTtoS = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if ((c1 in mapStoT and mapStoT[c1] != c2) or
                (c2 in mapTtoS and mapTtoS[c2] != c1)):
                return False
            
            mapStoT[c1] = c2
            mapTtoS[c2] = c1

        return True
