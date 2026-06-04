class Solution {
    public boolean isPalindrome(String s) {
        // So we know we only want alpha numberic answers. in this case what we can do is have two pointers, one that starts at the end of the string 
        // And one that starts and the beginning of the string. We want to skip all non alpha numberic, while still in  validitiy
        // Then we want to compare the left most char to the right most char, we do this until l < r.
        // this also ensures we only traverse once so worst case time complexity is O(1).

        int l = 0;
        int r = s.length() - 1;

        while (l < r) {
            while (l < r && !Character.isLetterOrDigit(s.charAt(l))) {
                l += 1;
            }

            while (l < r && !Character.isLetterOrDigit(s.charAt(r))) {
                r -= 1;
            }

            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) {
                return false;
            }

            l += 1;
            r -= 1;
        }
        
        return true;
    }
}
