class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []
        for p in perms: #[2,3], [3,2]
            for i in range(len(p) + 1):
                p_cpy = p.copy()
                p_cpy.insert(i, nums[0])
                res.append(p_cpy)
        return res
