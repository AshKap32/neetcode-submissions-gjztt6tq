class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Have a hashmap that has the key being the sorted version of a word
        Map<String, List<String>> grams = new HashMap<>();

        for (String str : strs) {
            char[] ch = str.toCharArray();
            Arrays.sort(ch);
            String sortedWord = new String(ch);
            if (!grams.containsKey(sortedWord)) {
                grams.put(sortedWord, new ArrayList<>());
            }
            grams.get(sortedWord).add(str);
        }

        return new ArrayList<>(grams.values());
    }
}
