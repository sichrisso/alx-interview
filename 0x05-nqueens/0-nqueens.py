class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []

        #intialize the board
        board = [['.']*n for i in range(n)]

        #create a hash map of column, row , diagonal left and right in order to see if the queens can attack each other.
        queenColumn = {}
        queenRow = {}
        queenDiagonalLeft = {}
        queenDiagonalRight = {}

        #validate the row,column and diagonal before putting a queen
        def valid(row, col):
            return not (row in queenRow or col in queenColumn or row + col in queenDiagonalLeft or row - col in queenDiagonalRight)

        
        def backtrack(row):
            #base case if we finish the board we have found a way to put all the queens
            if row == n:
                newBoard = []
                for i in range(n):
                    newBoard.append(''.join(board[i]))
                output.append(newBoard)
                return

            #iteratively put and backtrack the queens
            for i in range(n):
                if valid(row,i):
                    queenColumn[i] = True
                    queenRow[row] = True
                    queenDiagonalLeft[row+i] = True
                    queenDiagonalRight[row-i] = True
                    board[row][i] = 'Q'

                    backtrack(row+1)

                    board[row][i] = '.'
                    queenColumn.pop(i)
                    queenRow.pop(row)
                    queenDiagonalLeft.pop(row+i)
                    queenDiagonalRight.pop(row-i)


        backtrack(0)

        return output