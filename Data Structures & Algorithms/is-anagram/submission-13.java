class Solution {
    public boolean isAnagram(String s, String t) {
        int[] comp = new int[26];
        int[] main = new int[26];

        if (s.length() != t.length()) {
            return false;
        }

        for (int i = 0; i < s.length(); i++) {
            main[s.charAt(i) - 'a'] += 1;
            main[t.charAt(i) - 'a'] -= 1;
        }

        return Arrays.equals(comp, main);
    }
}
