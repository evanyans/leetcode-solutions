class Solution:
    # Attempted 3/1/2025
    # AHA: same as counting islands with minor modification to add a counter.
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1, 0), (-1, 0), (0, -1)]
        seen = set()
        m = len(grid) # rows
        n = len(grid[0]) #columns
        max_area = 0

        # check if within range and if we have "1"
        def valid(row, col): 
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1
        def dfs(row, col):
            area = 1
            for dx, dy in directions:
                next_row = row + dy
                next_col = col + dx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    area += dfs(next_row, next_col)
            return area
            
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row, col) not in seen:
                    seen.add((row, col))
                    max_area = max(max_area, dfs(row, col))

        return max_area
