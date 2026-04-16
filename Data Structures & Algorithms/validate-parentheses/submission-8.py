class Solution:
    def isValid(self, s: str) -> bool:
        # Create a hashmap to map the opening brackets to
        key = {'}':'{', ']':'[', ')': '('}

        # Create a stack to add the opening brackets to
        stack = []

        # once we get to a closing bracket  we chcek to see if the last value [-1] is == to the closing brracket
        # we are currently on, that ensures the opening and closing brackets are in the rigth order and correct type
        # at the end ifthe stack is empty we return true, assuming we havent returned false in the middle of it

        for bracket in s:
            # O(1) lookup and checks if its an oepnign ot closing bracket
            if bracket in key:
                # checks to see if the opening bracket in the stack == the closing brackets key (opening bracket)
                # Checks for order here as well as right type of bracket
                if stack and key[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False   
            else:
                # Add opening bracket into the stack
                stack.append(bracket)
        
        return stack == []

