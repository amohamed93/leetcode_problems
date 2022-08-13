import collections
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # without_duplication = list(set(nums))
        # print(len(without_duplication))
        # for elem in without_duplication:
        #     if nums.count(elem) > 1:
        #         return elem
        return [item for item, count in collections.Counter(nums).items() if count > 1][0]