class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Can have a running total and a count so every time we hit that number we increment the count
        # and see if that total ever hits k can basically we can scan to see if the complement of the current value is in the array
        # if that complement is in the array
        freq = defaultdict(int)
        freq[0] = 1
        curr = 0
        res = 0
        for num in nums:
            # add num to current sum
            curr += num
            diff = curr - k

            # if the diff (a previous prefixSum) exists in the map then we add it to res since thats how many values (running subarray totals) can add upto k
            res += freq[diff]
            freq[curr] += 1
        return res

