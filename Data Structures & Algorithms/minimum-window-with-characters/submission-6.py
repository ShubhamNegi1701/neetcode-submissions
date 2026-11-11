class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        counterT = Counter(t)
        window = {}

        res = [-1, -1]
        min_res_len = float("inf")

        have = 0
        need = len(counterT)

        l = 0
        r = 0

        while r < len(s):
            if s[r] in counterT:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] == counterT[s[r]]:
                    have += 1
        
            while have == need:
                window_length = r - l + 1
                if window_length < min_res_len:
                    min_res_len = window_length
                    res = [l, r]

                if s[l] in counterT:

                    window[s[l]] -= 1
               
                    if window[s[l]] < counterT[s[l]]:
                        have -= 1
                l += 1
                
            r += 1

        if min_res_len != float("inf"):
            return s[res[0]: res[1] + 1]
        else:
            return ""



                


        

       
        # if not t or not s:
        #     return ""

        # countT = Counter(t)
        # window = {}

        # have = 0
        # need = len(countT)

        # res = [-1, -1]
        # res_len = float("inf")

        # l = 0

        # r = 0
        # while r < len(s):
        #     c = s[r]
        #     window[c] = window.get(c, 0) + 1

        #     if c in countT and window[c] == countT[c]:
        #         have += 1

        #     while have == need:
        #         if (r - l + 1) < res_len:
        #             res_len = r - l + 1
        #             res = [l, r]
        #         window[s[l]] -= 1
        #         if s[l] in countT and window[s[l]] < countT[s[l]]:
        #             have -= 1
        #         l += 1

        #     r += 1

        # if res_len != float("inf"):
        #     return s[res[0]: res[1] + 1]
        # else:
        #     return ""

        

