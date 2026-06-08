class Solution {
    public int lengthOfLongestSubstring(String s) {
       // So obviorusly we can do a brute force where we have two nested for loops iterating over the 
       // array but that makes the time complexity O(n^2), so in this case what we could do 
       // is iterate with two pointers, the first pointer signifying what the last valid window start
       // is from and the second iterating over the entire array. we can also keep track of the letters we
       // have seen using a set, this allows for o(1) lookup, we would also ened a tracker for the longest string
        int l = 0;
        int r = 0;
        int longest = 0;
        Set<Character> seen = new HashSet<>();


        // then we can iterate until r reaches the end of the array (so full iteration is only o(n))
        while (r < s.length()) {
            
            // first i am going to check if we still have a valid window state
            while (seen.contains(s.charAt(r))) {
                seen.remove(s.charAt(l++));
            }

            // Now that we have a valid state
            seen.add(s.charAt(r));
            longest = Math.max(longest, r - l + 1);
            r++;

        }

        return longest;


    }
}
