class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # In order to achieve the best possible time compexity we can use bucket sort
        # That would provide us with an O(n) implementation, however if we have a time constraint then using the built in 
        # function may be a better idea however the worst case time complexity then would be O(nlogn)

        #First approach

        # Calculate the frequency 
        f_map = defaultdict(int)
        for num in nums:
            f_map[num] += 1


        # sort the f_map based on the value
        sorted_map = sorted(f_map.items(), key=lambda item: item[1])
        res = []
        while k > 0:

            res.append(sorted_map[-k][0])
            k -= 1

        return res
            

