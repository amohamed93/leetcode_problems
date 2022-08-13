class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set([each_el for each_el in nums1 if each_el in nums2]))