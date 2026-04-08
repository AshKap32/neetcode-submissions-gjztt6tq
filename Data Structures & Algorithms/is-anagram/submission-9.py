class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        A word is an anagram if it contains the same freqency of character as 
        one another. So what we can do is iterate of one string, grab the letters
        and map them to the freqency. In another loop we can loop over t and check 
        if the char we are on is in the map, AND then to check the freq and dec it by 1.
        Once the freq is 0 we remoce it from the array.

        The flaw with this technique is it keeps track of a hashmap which increases the space complexity
        Where as there is another method to track the count and thats to use ord(a) to get a count for the
        word in ASCII. We can make the ord(a) be the 0th and keep a track of ther two counts and comp once done w loop.
        """
        
        if len(s) != len(t): 
            return False
        
        count_s = defaultdict(int)
        count_t = defaultdict(int)

        for i in range(len(s)):
            count_s[s[i]] += ord(s[i]) - ord("a")
            count_t[t[i]] += ord(t[i]) - ord("a")
        
        return count_s == count_t
