class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## Can use bucket sorting for this where the index hold the values
        ## of the freqencies 

        ## Or the other way is to have the freq map of the elements 
        ## Then we can sort the dict based on freq and return the 
        ## Values based on that O(nlogn) time becuase of sort 
        ## algo and o(n) space complexity becuase of map


        # Can use bucket sort to sort based on the index, and extrat from there 
        # that would be o(1) access and o(n) worst case time 

        # but we can just track via a hashmap to count the freq, then sort the freq based on the items
        
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1
        
        sorted_map = sorted(freq_map.items(), key=lambda item: item[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_map[i][0])
        
        return res
        # freq_map = defaultdict(int)

        # for num in nums:
        #     freq_map[num] += 1

        # # sorted_freq = sorted(freq_map.items(), key=lambda item: item[1], reverse=True)

        # # res = []
        # # for i in range(k):
        # #     res.append(sorted_freq[i][0])

        # # return res

        # buckets = [[] for i in range(len(nums) + 1)]
        # # buckets = [[]] * len(nums)

        # for num, freq in freq_map.items():
        #     buckets[freq].append(num)
        
        # res = []

        # for bucket in buckets[::-1]:
        #     while k > 0 and bucket:
        #         res.append(bucket[-1])
        #         bucket.pop()
        #         k -= 1
            
            

        # return res


        

            

