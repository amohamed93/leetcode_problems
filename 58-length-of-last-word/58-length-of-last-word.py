class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_array = s.split(' ')
        all_char_list = [el for el in split_array if len(el) != 0]
        return len(all_char_list[-1])