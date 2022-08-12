class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ''.join([str(digit)for digit in digits])
        number = int(number) + 1
        number = list(str(number))
        return number