class Solution:
    # Attempted 4/1/2025
    # AHA: the divsion //3 for detemring square set location.
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for row in range(9):
            for col in range(9):
                # make a set
                if board[row][col] == '.':
                    continue
                if (board[row][col] in rows[row]
                or board[row][col] in cols[col]
                or board[row][col] in squares[(row // 3, col//3)]):
                    return False

                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                # Adding to the square specific set
                squares[(row // 3, col // 3)].add(board[row][col])
        return True
