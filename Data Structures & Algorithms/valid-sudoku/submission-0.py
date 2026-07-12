from collections import Counter

class Solution:
    def validateSeq(self, seq: List[str]) -> bool:
        counter = Counter(seq)

        for num, c in counter.items():
            if num == '.':
                continue

            if c > 1:
                return False
        
        return True

    def validateRow(self, board: List[List[str]], rowi: int) -> bool:
        row = board[rowi]
        return self.validateSeq(row)
        
    
    def validateCol(self, board: List[List[str]], coli: int) -> bool:
        col = []

        for row in board:
            col.append(row[coli])
        
        return self.validateSeq(col)
    
    def validateSquare(self, board: List[List[str]], square_i: int, square_j: int) -> bool:
        sq = []

        for i in range(3):
            rowi = square_i*3 + i
            for j in range(3):
                coli = square_j*3 + j

                sq.append(board[rowi][coli])

        return self.validateSeq(sq)
         
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for rowi in range(9):
            if not self.validateRow(board, rowi):
                return False
        
        for coli in range(9):
            if not self.validateCol(board, coli):
                return False

        for i in range(3):
            for j in range(3):
                if not self.validateSquare(board, i, j):
                    return False

        return True
        