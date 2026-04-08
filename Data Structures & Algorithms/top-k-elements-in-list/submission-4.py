class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## Can use bucket sorting for this where the index hold the values
        ## of the freqencies 

        ## Or the other way is to have the freq map of the elements 
        ## Then we can sort the dict based on freq and return the 
        ## Values based on that O(nlogn) time becuase of sort 
        ## algo and o(n) space complexity becuase of map

        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1

        sorted_freq = sorted(freq_map.items(), key=lambda item: item[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_freq[i][0])

        return res

        

            

