class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        #find peak
        l, r = 1, length - 2
        while l <= r:
            m = (l + r) // 2
            left, mid, right = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)
            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        peak = m

        #search left
        l, r = 0, peak
        while l <= r:
            m = (r + l) // 2
            if mountainArr.get(m) < target:
                l = m + 1
            elif mountainArr.get(m) > target:
                r = m - 1
            else:
                return m
        
        #search right
        l, r = m, length - 1
        while l <= r:
            m = (r + l) // 2
            if mountainArr.get(m) > target:
                l = m + 1
            elif mountainArr.get(m) < target:
                r = m - 1
            else:
                return m

        return -1






