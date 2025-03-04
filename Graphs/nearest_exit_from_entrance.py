class Solution:
    # Attempted 3/2/2025
    # AHA: remember to initialize seen to the entrance, and the queue to the entrance.
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and maze[row][col] == '.'
        def border(row, col):
            return not ( 0 <= row < m and  0 <= col < n )

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m = len(maze) # rows
        n = len(maze[0]) # columns

        seen = {(entrance[0], entrance[1])}
        queue = deque([(entrance[0], entrance[1], 0)])
        while queue:
            
            row, col, steps = queue.popleft()

            for dx, dy in directions:
                next_row = row + dy
                next_col = col + dx
                   
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
                if border(next_row, next_col) and steps != 0: 
                    return steps
        
        return -1
