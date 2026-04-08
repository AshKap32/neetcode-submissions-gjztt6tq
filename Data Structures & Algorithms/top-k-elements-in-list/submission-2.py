from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Map for value and its freqency
        res = []
        freq = defaultdict(int)

        for num in nums: # O(n)
            freq[num] += 1
        
        sorted_tuple = sorted(freq.items(), key= lambda num: num[1], reverse=True) # O(nlogn)
        
        print(sorted_tuple)
        for i in range(k): 
            res.append(sorted_tuple[i][0])
        
        return res
