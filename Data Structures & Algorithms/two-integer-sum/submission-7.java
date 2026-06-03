class Solution {
    public int[] twoSum(int[] nums, int target) {
        // We know that one pair of indicies satisfies the condition
        // So the next step would be to create a map of the values we have and the index its mapped too

        // we can then iterate over nums and check to see if the complament exists in the map (this provides us O(1) look up since we are using a hashmap and not an array)

        Map<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int comp = target - nums[i];
            if (seen.containsKey(comp)) {
                return new int[]{seen.get(comp), i};
            }
            seen.put(nums[i], i);
        }

        return new int[]{};
    }
}
