class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        # go right to left, start at the position closest to target
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p)/s)
            #apply collision
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)