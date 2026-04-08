class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) < 1:
            return [0]

        
        results = []
        
        for left in range(len(temperatures)):

            right = left + 1
            while right < len(temperatures):
                if temperatures[right] > temperatures[left]:
                    results.append(right-left)
                    break
                right += 1

            if right == len(temperatures):
                results.append(0)

        return results 