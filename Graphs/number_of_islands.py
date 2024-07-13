class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        explored = set()
        width = len(grid[0]) - 1
        height = len(grid) - 1

        def search(grid):
            counter = 0
            for i, m in enumerate(grid):
                for j, n in enumerate(grid[i]):
                    print(counter)
                    if (j, i) not in explored and n == "1":
                        dfs(j, i, grid)
                        counter += 1
            return counter

        def dfs(x, y, grid):
            if (x, y) in explored:
                return
            explored.add((x, y))
            if x > 0 and grid[y][x-1] == "1":
                dfs(x-1, y, grid)
            if x < width and grid[y][x+1] == "1":
                dfs(x+1, y, grid)
            if y < height and grid[y+1][x] == "1":
                dfs(x, y+1, grid)
            if y > 0 and grid[y-1][x] == "1":
                dfs(x, y-1, grid)

        return search(grid)


