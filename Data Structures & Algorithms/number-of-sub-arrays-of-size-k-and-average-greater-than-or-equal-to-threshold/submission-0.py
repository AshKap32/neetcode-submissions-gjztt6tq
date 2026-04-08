class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        seen = []
        num_sub = 0
        left = 0
        total = 0

        for right in range(len(arr)):
            total += arr[right]
            seen.append(arr[right])

            if right - left + 1> k:
                total -= arr[left]
                seen.remove(arr[left])
                left += 1

            if right - left + 1 == k:
                if total /k >= threshold:
                    num_sub += 1

        return num_sub
