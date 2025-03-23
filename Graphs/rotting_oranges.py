class Solution:
    # Attempted 3/22/2025
    # AHA: ONLY PROCESS STAGE BY STAGE LAYER BY LAYER, i.e. EXTRZ FOR LOOP
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1
        m = len(grid)
        n = len(grid[0])

        seen = set()
        # lets iterate the entire matrix until we find at least
        # one orange 
        queue = deque()
        fresh = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        
        ans = 0
        while queue and fresh:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dx, dy in directions:
                    next_row, next_col = row + dy, col + dx
                    if valid(next_row, next_col) and (next_row, next_col) not in seen:
                        seen.add((next_row, next_col))
                        grid[next_row][next_col] += 1 
                        fresh -= 1
                        queue.append((next_row, next_col))
            ans += 1
        return ans if fresh == 0 else -1
