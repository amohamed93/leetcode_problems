class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            generate_str = list(haystack.replace(needle, '*'))
            return generate_str.index('*')
            
        