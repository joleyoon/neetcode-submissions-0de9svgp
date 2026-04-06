class Solution:
    def binarysearch(self, l, r, nums, target):
        if l > r:
            return -1

        m = l + (r - l) // 2

        if nums[m] == target:
            return m
        elif nums[m] > target:
            return self.binarysearch(l, m - 1, nums, target)
        else:
            return self.binarysearch(m + 1, r, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binarysearch(0, len(nums) - 1, nums, target)