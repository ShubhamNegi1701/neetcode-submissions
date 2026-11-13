class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj = { c:set() for w in words for c in w }

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visiting = set()
        visited = set()
        res = []

        def dfs(ch):
            if ch in visiting:
                return False
            if ch in visited:
                return True

            visiting.add(ch)

            for nei in adj[ch]:
                if not dfs(nei):
                    return False

            visiting.remove(ch)
            visited.add(ch)
            res.append(ch)

            return True
        
        for char in adj.keys():
            if not dfs(char):
                return ""

        res.reverse()
        return "".join(res)
            






        # adj = { c:set() for w in words for c in w }

        # for i in range(len(words) - 1):
        #     w1, w2 = words[i], words[i + 1]
        #     minLen = min(len(w1), len(w2))
        #     if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
        #         return ""
        #     for j in range(minLen):
        #         if w1[j] != w2[j]:
        #             adj[w1[j]].add(w2[j])
        #             break


        # # Step 3: DFS for Topological Sort (True = Valid / Can finish)
        # visiting = set()  # Currently in the recursion stack
        # visited = set()   # Successfully processed
        # res = []

        # def dfs(char: str) -> bool:
        #     if char in visiting:
        #         return False  # Cycle detected -> invalid ordering
        #     if char in visited:
        #         return True   # Already safely processed

        #     visiting.add(char)

        #     for neighbor in adj[char]:
        #         if not dfs(neighbor):  # Neighbor encountered a cycle
        #             return False

        #     visiting.remove(char)
        #     visited.add(char)
        #     res.append(char)
        #     return True       # Subtree is valid

        # # Run DFS for every character
        # for char in adj:
        #     if not dfs(char):  # If validation failed, return ""
        #         return ""

        # # Post-order DFS yields reverse topological order
        # res.reverse()
        # return "".join(res)