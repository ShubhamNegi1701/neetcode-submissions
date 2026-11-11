class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counterElements = {}
        max_freq = 0
        max_len = 0

        for r in range(len(s)):
            # add new element to counter
            counterElements[s[r]] = counterElements.get(s[r], 0) + 1

            for key, count in counterElements.items():
                if count > max_freq:
                    max_freq = count

            while (r - l + 1) - max_freq > k:
                counterElements[s[l]] -= 1
                l += 1

            # window length - max frequency < k = valid
            if (r - l + 1) - max_freq <= k:
                if r - l + 1 > max_len:
                    max_len = r - l + 1

        return max_len
        