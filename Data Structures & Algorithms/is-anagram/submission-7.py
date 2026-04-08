class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Can compare the two freqencies, using a hashmap iteration for one of the values 
        # and then iterating over the second stirng, seeing if the value is in the map, if it is then decrease the freq, if the new freq is 0 remove from the map
        # if you get out of that for loop then you can return True
        #Time complexity here would be O(n)
        #Trade off is it would take longer to code up this solution
        # A quicker method would be to check if the two words sorted are equivalent
        #Worst case time complexity is O(nlogn) since thats the sort systems time complexity 

        if sorted(s) == sorted(t):
            return True

        return False