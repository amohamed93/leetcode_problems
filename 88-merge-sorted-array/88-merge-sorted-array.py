class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums = sorted(nums1[0: m]+nums2[0: n])
        index = 0
        for num in nums:
            nums1[index] = num
            index += 1
        