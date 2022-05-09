class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        non_zero_arr = filter(lambda num: num != 0, nums)
        zero_arr = filter(lambda num: num == 0, nums)
        merge_arr = [*list(non_zero_arr), *list(zero_arr)]
        for i in range(0, len(nums)):
            nums[i] = merge_arr[i]
