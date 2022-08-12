class Solution:
    def romanToInt(self, s: str) -> int:
        convert_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        index = 0
        number = 0
        for each_char in list(s):
            if index > len(s) - 1:
                break
            value = convert_dict[s[index]]
            if index + 1 < len(s) and convert_dict[s[index]] < convert_dict[s[index+1]]:
                value = -1 * value + convert_dict[s[index+1]]
                index += 1     
            number += value
            index += 1
        return number