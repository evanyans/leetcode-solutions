class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # 0 is a gate
        # -1 is a wall
        # INF can be traversed
        m = len(grid)
        n = len(grid[0])
    
        queue = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r, c))

        seen = set()
        ans = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 2147483647

        level = 0
        while queue:
            level += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dx, dy in directions:
                    next_row, next_col = row + dy, col + dx
                    if valid(next_row, next_col) and (next_row, next_col) not in seen:
                        seen.add((next_row, next_col))
                        grid[next_row][next_col] = level
                        queue.append((next_row, next_col))
                    

            
            
        
