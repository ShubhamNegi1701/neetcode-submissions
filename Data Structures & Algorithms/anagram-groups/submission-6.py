class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        res = []

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            anagrams[tuple(key)].append(s)

        for anagram in anagrams.values():
            res.append(anagram)

        return res

