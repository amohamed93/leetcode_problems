class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int(''.join([str(digit)for digit in digits])) + 1
        number = list(str(number))
        return number