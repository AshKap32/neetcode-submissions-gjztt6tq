class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## You can iterate through each row and column in a for loop
        ## Have some sort of seen map that tracks to see if there is a value already in that 
        ## Have another seen set that tracks to see if the 3x3 grid has duplicates
        ## once column hits 3, move to adding to the next 3x3 part of the set
        ## Check to see if that value already exists in that set if it does return false
        
        #Key = Row #/Col #/ Square # (3x3 so row // 3 and cols // 3); Value = Set
        # Since any value in a 3x3 square grid would have the same value for row //3 and col //3
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        ## Pattern is we do not want duplicates, we want quick lookup based on index
        ## So hash set
        for row in range(len(board)):
            for col in range(len(board[row])):
                print(len(board), len(board[row]))
                if board[row][col] == '.':
                    continue 

                ## Valid only if value is not already in this rows row set
                ## Valid only if value is not arleady in this cols col set
                ## Valid only if value is not in this row/col tuple set
                if (board[row][col] in rows[row] or
                    board[row][col] in cols[col] or
                    board[row][col] in square[(row // 3, col // 3)]):
                    return False

                # its a set, so cant use = op since its not just one value, we need to add that that rows set
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                square[(row // 3, col // 3)].add(board[row][col])
        return True
                