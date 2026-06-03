class Solution {
    public boolean isAnagram(String s, String t) {
        // Anagrams means that they are equal to each other, there are two ways we can do this
        // the first one is using a sorting algorithm, if both are equivlent when sorted
        // They are anagrams of each other. 

        char[] sortedS = s.toCharArray();
        char[] sortedT = t.toCharArray();

        Arrays.sort(sortedS);
        Arrays.sort(sortedT);

        return Arrays.equals(sortedS, sortedT);


    }
}
