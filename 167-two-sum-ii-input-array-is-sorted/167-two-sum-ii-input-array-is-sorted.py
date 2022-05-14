import numpy as np
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for each_el in set(numbers):
            if target - each_el in numbers and target - each_el != each_el:
                return sorted([numbers.index(each_el) +1, numbers.index( target - each_el)+1])
            elif target - each_el == each_el:
                values = np.array(numbers)
                searchval = each_el
                ii = sorted([x + 1 for x in np.where(values == searchval)[0][:2]])
                return ii