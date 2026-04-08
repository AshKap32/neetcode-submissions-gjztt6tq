class Solution:
    def isValid(self, s: str) -> bool:
        
        # bracket map mapping close to open pranthesis 
        # stack that we push all open brackets to
        # check if the stack exists and if the last value in the stack (last open bracket)
        # Matches the closing bracket we have 
        # To do this we map the closing bracket to opening and check if the closing value 
        # is equal to the opening value
        # If it isnt anuy one of those we return false.
        # else pop last from stack
        # Stack operations are o(1) Last in First out

        bracket_map = {")": "(", "]":"[", "}":"{"}
        stack = []

        for ch in s:
            if ch in bracket_map:
                if stack and stack[-1] == bracket_map[ch]:
                    # Pop takes an index or just removes the last one if no index
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        ## Only return true if the stack is empty if it isnt all brackets havent been paired
        return True if not stack else False