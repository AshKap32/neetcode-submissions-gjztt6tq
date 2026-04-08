class MinStack:

    def __init__(self):
        self.stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
       
        if not self.stack:
            return None
        
        minVal = self.stack[0]

        for num in self.stack[1:]:
            if num < minVal:
                minVal = num
        
        return minVal
       