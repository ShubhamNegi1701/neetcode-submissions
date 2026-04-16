class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        # create 26 length array x M
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            key = tuple(count)
            map[key] = map.get(key, []) + [word]
        return list(map.values())
            

        # for each item increment counter of element found 
        # store the array as key in map, with the element as a string
        # return values