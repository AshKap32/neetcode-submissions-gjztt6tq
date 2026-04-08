class Solution:

    def encode(self, strs: List[str]) -> str:
        ## String can be a multitude of lengths that we are putting in
        ## Need to have some sort of identfier on how long that string is
        ## As well as where the new string starts

        encoded = ""

        # Simple For loop for iterating accross the String
        for s in strs:
            # Idenify string via Length and Special Char
            encoded += str(len(s)) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        # Now that we have an identifying char and the string length 
        # We can Iterate of that String and append values from the
        # Starting till the len of that string
        # We want to iterate over the entire string length
        # Reason we would want the length here is, after getting to the special
        # Char we would know before that lies the amount that should be appended
        # into the result array for this string so its back to the orginal length

        res = []
        l = 0
        
        while l < len(s):
            # Setting the right value to the same positon as l at the start
            r = l
            # Going until r is at the special character (should usually only be 1 increment)
            while s[r] != '#':
                r += 1

            # Now that we are at teh special char for right, we know that the len is 1 behind that
            # and new string start is 1 above that, so we grab the length

            # Length = l to r to account for any integers > 9 sicne l is at
            # The starting index of the number (1 index above the end of the last string)

            length = int(s[l:r])

            # Start = Special Char Index + 1
            l = r + 1
            # End = Start + length 
            r = l + length 
            # Append to res using string spilcing non inclusive of end so r would be at next length
            res.append(s[l:r])

            # Bring left pointer to the next length
            l = r
        return res

            
    