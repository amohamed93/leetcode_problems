class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final_str = ''
        count = 0
        word1 = list(word1)
        word2 = list(word2)
        if len(word1) > len(word2):
            while count < len(word2):
                final_str += word1[count] + word2[count]
                count += 1
            final_str += ''.join(word1[count:])
        elif len(word1) < len(word2):
             while count < len(word1):
                final_str += word1[count] + word2[count]
                count += 1
             final_str += ''.join(word2[count:])
        else:
            while count < len(word1):
                final_str += word1[count] + word2[count]
                count += 1
        return final_str
        