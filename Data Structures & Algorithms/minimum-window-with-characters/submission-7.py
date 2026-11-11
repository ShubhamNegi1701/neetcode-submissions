class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        countT = Counter(t)
        window = {}

        res = [-1, -1]
        min_res_len = float("inf")

        have = 0
        need = len(countT)

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                curr_len = r + l + 1
                if curr_len < min_res_len:
                    min_res_len = curr_len
                    res = [l, r]

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
            l += 1
        l, r = res
        return s[l,r+1] if min_res_len != float("inf") else ""




        # if not s or not t:
        #     return ""

        # countT = Counter(t)
        # window = {}

        # res = [-1, -1]
        # min_res_len = float("inf")

        # have = 0
        # need = len(countT)

        # l = 0

        # for r in range(len(s)):
        #     c = s[r]
        #     window[c] = 1 + window.get(c, 0)    

        #     if c in counttT and window[c] == countT[c]:
        #         have += 1
            
        #     while have == need:
        #         #update our result
        #         if (r - l + 1) < min_res_len:
        #             res = [l, r]
        #             min_res_len = (r - l + 1)

        #         #pop from left of the window
        #         window[s[l]] -= 1
        #         if s[l] in countT and window[s[l]] < countT[c]:
        #             have -= 1
                
        #         l += 1

        # l, r = res
        # return s[l:r+1] if min_res_len != float("inf") else ""





                


        

       
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

        

