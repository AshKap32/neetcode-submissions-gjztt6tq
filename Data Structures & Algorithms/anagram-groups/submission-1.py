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

        for s in strs:
            # Have to join them together since sorted a string returns a list of chars
            sorted_w = "".join(sorted(s))
            res[sorted_w].append(s)
        

        #Convert to list since default dict returns values as tuples
        return list(res.values())