class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for each_el in set(numbers):
            if target - each_el in numbers and target - each_el != each_el:
                return sorted([numbers.index(each_el) +1, numbers.index( target - each_el)+1])
            elif target - each_el == each_el:
                return [index + 1 for index, num in enumerate(numbers) if num == each_el]
                