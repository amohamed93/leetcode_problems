class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_array = sorted(list(set(nums)), reverse=True)
        if len(sorted_array) >= 3:
            return sorted_array[2]
        else:
            return max(sorted_array)
        