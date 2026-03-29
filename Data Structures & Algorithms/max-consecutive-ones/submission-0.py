class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        curr = 0

        for num in nums:
            curr = curr + 1 if num == 1 else 0
            res = max(curr, res)
        
        return res
