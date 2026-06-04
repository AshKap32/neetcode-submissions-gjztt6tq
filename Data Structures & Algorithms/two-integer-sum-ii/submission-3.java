class Solution {
    public int[] twoSum(int[] numbers, int target) {
         // Input array is already sorted for us, so what we can do in order to use contant space instead of using a hashmap like before
         // is using some simple math, we know the total we have will vary, hwover if we add the total with two pointer,s one at the 
         // beginning and one at the end, what we can do instead is then add those numbers, check if its greater than or less than 
         // the target, if its greater than, we know the right side is too big since its sorted, and vice versa.
         // we do this until l < r or we find the result.
         // This gurantees a worst case time cmoplexity of O(n) jsut like the ahsmap usage EXCEPT with constant space

        int l = 0;
        int r = numbers.length - 1;
        
        while (l < r) {
            int total = numbers[l] + numbers[r];

            if (total > target) {
                r -= 1;
            } else if (total < target) {
                l += 1;
            } else if (total == target) {
                return new int[]{l + 1, r + 1};
            }
        }
        return new int[]{};
    }
}
