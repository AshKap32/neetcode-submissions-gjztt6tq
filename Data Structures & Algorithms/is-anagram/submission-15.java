class Solution {
    public boolean isAnagram(String s, String t) {
        // Anagrams means that they are equal to each other, there are two ways we can do this
        // the first one is using a sorting algorithm, if both are equivlent when sorted
        // They are anagrams of each other. 

        // char[] sortedS = s.toCharArray();
        // char[] sortedT = t.toCharArray();

        // Arrays.sort(sortedS);
        // Arrays.sort(sortedT);

        // return Arrays.equals(sortedS, sortedT);rhog

        // The Second way to do it is have a comparison array, and a main array where we make modifications
        // In the main array we loop through one of the strings, and what we can do is keep a constant 
        // or near constant space complexity becaue we know there are 26 alphabets.

        // we can create the two arrays of 0's for 26 letters
        int[] main = new int[26];
        int[] comp = new int[26];  

        if (s.length() != t.length()) {
            return false;
        }

        for (int i = 0; i < s.length(); i++) {
            // we can add to the main array with s an subtract with t. We can take chatAt - a because that will produce the right ascii
            // By the end the array should be back to default if the values in both are the same
            main[s.charAt(i) - 'a'] += 1;
            main[t.charAt(i) - 'a'] -= 1;
        }

        return Arrays.equals(main, comp);


    }
}
