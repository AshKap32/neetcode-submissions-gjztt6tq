class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        # if characters are more than 1 then we add the string and number to character and number to s 
        # at the end we append to the beginning of the array 
        # Theoretically, we can sort the list of chars so all values are together
        
        # chars.sort()
        temp_len = 1
        # initialize s
        s += chars[0]

        for i in range(1, len(chars)):
            char = chars[i]
            # adds char to the list if the last one is not the same
            if s[-1] != char:
                # If temp len is 1 then we just add the new character
                if temp_len == 1:
                    s += char
                else:
                    s += str(temp_len)
                    s += char
                # Either way reset temp len to 1 now that we have a new number
                temp_len = 1
            else:
                # Keep track of the len of the current char
                temp_len += 1

        # if we ended on a repeating character temp len would not just be one
        if temp_len != 1:
            s += str(temp_len)
        print(s)
        # convert s to a list and add it to the beginning of chars

        for i in range(len(s)):
            chars[i] = s[i]

        # chars = list(s) + chars

        return len(s)