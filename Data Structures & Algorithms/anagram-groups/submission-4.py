class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # The intuition here is we can find all anagrams by doing a one pass and creating a sort
        # Of the words and make that the key of the map if we find another sorted word to be similar we can add that into our list

        # anagrams = defaultdict(list)

        # for word in strs:
        #     # Joining the word since sorted(word) returns a list of characters
        #     sorted_w = "".join(sorted(word))
        #     anagrams[sorted_w].append(word)

        # # Converting the default dict values into an array of arrays

        # return list(anagrams.values())

        ana = defaultdict(list)

        for word in strs:
            # sort each of the words to get the key
            sorted_w = "".join(sorted(word))
            # combine them based on the key
            ana[sorted_w].append(word)
        

        # want the values, so convert the values to a list
        return list(ana.values())
