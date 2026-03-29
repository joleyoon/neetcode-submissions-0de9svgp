class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = j = 0

        for i in range(len(nums)):
            if nums[i] != val:
                cnt += 1
                nums[j] = nums[i]
                j += 1
            
        return cnt
