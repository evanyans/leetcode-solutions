class Solution:
    # Attempted 3/21/2025
    # AHA moment: my logic was 100% correct, i was just iteratig the wrong border values the entire time
    # !!! PLEASE DOUBLE CHECK THE EASY PARTS BEFORE CHECKING THE LOGIC !!!!
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # idea is to dfs from the pacific
        #            dfs from the atlantic
        # if their end node has a path for both, its valid thus add to answer
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        ans = []
        seen = set()
        m = len(heights)
        n = len(heights[0])

        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
            
        def dfs(row, col, ocean):
            # do the visited check before, because we must add visited ASAP!
            if (row, col) in ocean:
                return
            ocean.add((row, col))
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if (valid(next_row, next_col) and 
                    heights[next_row][next_col] >= heights[row][col] and
                    (next_row, next_col) not in ocean):
                    dfs(next_row, next_col, ocean)
    
        # Let's iterate just the border and do a dfs on each node
        pacific_visited = set()
        atlantic_visited = set()
        for i in range(m):
            dfs(i, 0, pacific_visited)  # Left border (Pacific)
            dfs(i, n - 1, atlantic_visited)  # Right border (Atlantic)
        
        # Start DFS from all Atlantic border cells
        for j in range(n):
            dfs(0, j, pacific_visited)  # Top border (Pacific)
            dfs(m - 1, j, atlantic_visited)  # Bottom border (Atlantic)
        
        return list(pacific_visited.intersection(atlantic_visited))



        
