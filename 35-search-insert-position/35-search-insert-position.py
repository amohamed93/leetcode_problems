class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            filtered_list = filter(lambda num : num < target, nums)
            return len(list(filtered_list))