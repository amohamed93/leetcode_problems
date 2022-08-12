class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for num in list(set(nums)):
            if nums.count(num) == 1:
                return num
            