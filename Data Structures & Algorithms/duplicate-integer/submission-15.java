class Solution {
    public boolean hasDuplicate(int[] nums) {
        // What we can do is go through the nums list and check to see if it is in our seen set
        // If it is then we return true, else we add the currnet number to the seen set

        Set<Integer> seen = new HashSet<>();

        for (int num : nums) {
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}