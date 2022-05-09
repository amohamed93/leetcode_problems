class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([each_num * each_num for each_num in nums])