class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map = defaultdict(int)

        for s_char in s:
            freq_map[s_char] += 1
        
        for char in t:
            if char in freq_map:
                if freq_map[char] - 1 == 0:
                    freq_map.pop(char)
                else:
                    freq_map[char] -= 1
            else:
                return False
        if freq_map:
            return False
        else:
            return True
        
