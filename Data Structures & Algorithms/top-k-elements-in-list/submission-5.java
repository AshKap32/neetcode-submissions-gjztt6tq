class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // We can iterate over to track the the freqency of each character, then we can sort based
        // on the frequency (nlogn operation). and becuase we are iterating in another step thats o(n)
        // Worst case time cmoplexity is going to be o(nlogn) in this case
        // HashMap Provides O(1) lookup which is why we're using this since we need to pull the number we are adding the freq for

        Map<Integer, Integer> freq = new HashMap<>();

        for (int num : nums) {
            // if it doesn't exists this puts it in there and updates the value
            freq.put(num, freq.getOrDefault(num, 0) + 1);

        }

        List<Map.Entry<Integer, Integer>> freqs = new ArrayList(freq.entrySet());

        freqs.sort(Map.Entry.<Integer, Integer>comparingByValue().reversed());
        
        int[] res = new int[k];

        for (int i = 0; i < k; i++) {
            // Appends the key (the value we need) to the res
            res[i] = freqs.get(i).getKey();
        }

        return res;

    }
}
