class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // In order for a word to be an anagram, they have to have the same letters, 
        // Theoretically if you sort the word, all anagrams of the word will be the same sorted
        // Therefore we can use that to be our key

        // Create a HashMap, that provide O(1) lookup to see if the key exists, else we make one.
        // Want an array list since its a dynamic size
        Map<String, List<String>> anagrams = new HashMap<>();

        for (String s : strs) {
            // First thing first, need to sort this string I have 
            char[] charS = s.toCharArray();
            Arrays.sort(charS);
            String sortedS = new String(charS);

            // If Anagrams does not contain the key for this word, then we create an empty list
            if (!anagrams.containsKey(sortedS)) {
                anagrams.put(sortedS, new ArrayList<String>());
            }

            // Now that this key exsists, we add the orginal string to this list
            anagrams.get(sortedS).add(s);
        }
        
        // Return an ArrayList of Values
        return new ArrayList<List<String>>(anagrams.values());
    }
}
