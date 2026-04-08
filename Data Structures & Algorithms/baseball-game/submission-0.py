class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Can pop from the top of the stack, store the rules for what
        # Happends in a hashmap which will look for the vlaue thats popped
        # if its a number, nothing ill happend, but if its in the map then
        # we will take the numbers in the new popped res array and perform the action
        # Either Addition, Popping last added value from the stack, or doubling the last record
        # once at the end sum together the record array

        record = []
        ops = {"+", "D", "C"}

        for i, op in enumerate(operations):
            if op in ops:
                if op == "+":
                    add = sum(record[-2:])
                    record.append(add)
                if op == "D":
                    dub = record[-1] * 2
                    record.append(dub)
                if op == "C":
                    record.pop()
            else:
                # Add them in as an int and not a str
                record.append(int(op))
        

        return sum(record)

