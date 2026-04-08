class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
                # I can take the first word as a refernce word and while we arent at the end of the list
        # We can check to see if word[i] i is the pointer for the characters == list[j][i] j is the pointer for the next word. Reset the J counter at the end of the list. if they are the same and we ahve a bool value that gets switched from true to false we can return the output string

        res = ""
        bool_val = True
        min_len = min(len(s) for s in strs) #O(N)
        first = strs[0]

        i = 0 
        # O(m)
        while bool_val and i < min_len:
            j = 1
            while j < len(strs): # O(N)
                if first[i] == strs[j][i]:
                    j += 1
                else:
                    bool_val = False
                    break
            # if we broke out of here and have not returned out of the main while loop
            if bool_val:
                res += first[i]
                i += 1

        return res

        # Time Complexity O(N*M)space complexity is O(1) N = Number of items in the list, M is len of minimum word