class Solution:
    # Attempted 3/20/2025
    # AHA: Anything thats not the border or connected to the border should be swapped to X's
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # idea is, we will DFS on the entire border looking for O's
        # any O's we find will be marked in the safe set

        # then we will iterate the matrix and change any unsafe O's to X's
        def dfs(row, col):
            for dx, dy in directions:
                next_row = row + dy
                next_col = col + dx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    dfs(next_row, next_col)

        graph = defaultdict(list)
        directions = [(0,1), (1, 0), (-1, 0), (0, -1)]
        m = len(board)
        n = len(board[0])
        seen = set()
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and board[row][col] == "O"
        for row in [0, m - 1]:
            for col in range(n):
                if board[row][col] == "O" and (row, col) not in seen:
                    seen.add((row, col))
                    dfs(row, col)
        for row in range(m):
            for col in [0, n-1]:
                if board[row][col] == "O" and (row, col) not in seen:
                    seen.add((row, col))
                    dfs(row, col)

        # Set all unsafe O's to X's
        for row in range(m):
            for col in range(n):
                if board[row][col] == "O" and (row, col) not in seen:
                    board[row][col] = "X"
        return
