class Solution:
  # Attempted 3/31/2025
  # AHA: brutha its backtracking + dfs, not just dfs bra
    def exist(self, board: List[List[str]], word: str) -> bool:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        m = len(board)
        n = len(board[0])
        
        seen = set()
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        def backtrack(row, col, i, seen):
            if i == len(word):
                return True
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if (valid(next_row, next_col) and (next_row, next_col) not in seen and
                    board[next_row][next_col] == word[i]):
                    seen.add((next_row, next_col))
                    if backtrack(next_row, next_col, i + 1, seen):
                        return True
                    seen.remove((next_row, next_col))
        for row in range(m):
            for col in range(n):
                word_set = set(word)
                if board[row][col] == word[0] and backtrack(row, col, 1, {(row, col)}):
                    return True
        return False


        
