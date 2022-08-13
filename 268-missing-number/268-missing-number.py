class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        min_val = 0
        max_val = len(nums)
        while min_val <= max_val:
            if min_val not in nums:
                return min_val
            min_val += 1
            