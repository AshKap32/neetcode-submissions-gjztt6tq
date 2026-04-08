class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        res = ""
        n = r = len(word1)

        newWord = word1 + word2

        while l < n and r < len(newWord):
            res += newWord[l]
            res += newWord[r]
            l += 1
            r += 1
        
        while l < n:
            res += word1[l]
            l += 1
        
        while r < len(newWord):
            res += newWord[r]
            r += 1
        return res
        # while l < len(word1) and r < len(word2):
        #     res += word1[l]
        #     res += word2[r]
        #     l += 1
        #     r += 1

        # while l < len(word1):
        #     res += word1[l]
        #     l += 1

        # while r < len(word2):
        #     res += word2[r]
        #     r +=

        # return res