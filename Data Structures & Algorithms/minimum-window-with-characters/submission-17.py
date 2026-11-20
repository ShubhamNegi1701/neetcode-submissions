class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counterT = Counter(t)
        counterS = {}

        have = 0
        need = len(counterT)

        res = [-1, -1]

        l = 0

        resLen = float("inf")

        for r in range(len(s)):
            counterS[s[r]] = counterS.get(s[r], 0) + 1

            if s[r] in counterT and counterS[s[r]] == counterT[s[r]]:
                have += 1

            while have == need:
                currLen = r - l + 1
                if currLen < resLen:
                    resLen = currLen
                    res = [l, r]
                
                counterS[s[l]] -= 1

                if s[l] in counterT and counterS[s[l]] < counterT[s[l]]:
                    have -= 1

                l += 1

        return s[res[0]: res[1] + 1] if res != float("inf") else ""












        # if not s or not t:
        #     return ""
        
        # counterT = Counter(t)
        # counterS = {}

        # l = 0
        # res = [-1, -1]

        # need = len(counterT)
        # have = 0

        # resLen = float("inf")

        # for r in range(len(s)):
        #     counterS[s[r]] = counterS.get(s[r], 0) + 1

        #     if s[r] in counterT and counterS[s[r]] == counterT[s[r]]:
        #         have += 1

        #     while have == need:
        #         curr_len = r - l + 1
        #         if curr_len < resLen:
        #             resLen = curr_len
        #             res = [l , r]
                
        #         counterS[s[l]] -= 1

        #         if s[l] in counterT and counterS[s[l]] < counterT[s[l]]:
        #             have -= 1

        #         l += 1

        # return s[res[0]: res[1] + 1] if resLen != float("inf") else ""