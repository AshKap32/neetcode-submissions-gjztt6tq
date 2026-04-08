class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Pattern, we are tryign to return a list of lists, so 
        # The key would be something that matches values together
        # The Values would be stored in a list
        # Return the value

        # Two ways of doing this, the key for an anagram would be the same if the values were sorted
        ## or theyd be the sam i the count of the ASCII char were the same
        ## ASCII provides a better time completixty since the sortig is O(nlogn)
        ## Have a default Dict to take care of some edge cases
        # First Way
        res = defaultdict(list)

        # for s in strs:
        #     # Have to join them together since sorted a string returns a list of chars
        #     sorted_w = "".join(sorted(s))
        #     res[sorted_w].append(s)
        
        # More efficient method
        for s in strs:
            # For each string itll have 26 possible letter choices, create an array of that
            count = [0] * 26 
            # Time complexity for this is avergage length of the words O(n*m)
            for ch in s:
                # Ord is the ascii access, in order to make a start at 0 and up to 25 to match index
                # we need to subtract the current char ascii by ord("a") since ord(a) - ord(a) = 0
                count[ord(ch) - ord('a')] += 1
            
            # append the string utlizing the key as count, convert count to tuple
            res[tuple(count)].append(s)

        

        #Convert to list since default dict returns values as tuples
        return list(res.values())