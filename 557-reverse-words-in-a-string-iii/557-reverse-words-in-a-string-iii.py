class Solution:
    def reverseWords(self, s: str) -> str:
        list_s = s.split()
        return ' '.join([word[::-1] for word in list_s])