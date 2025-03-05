class Solution:
    # Attempted 3/5/2025
    # aha: my math was wrong for overlap, we are checking if one circle falls within
    # radius of another, not JUST an overlap
    # aha #2: i needed to reset seen set because we are doing indepedent DFS for each bomb
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # connect bombs that overlap to form a graph
        graph = defaultdict(list)
        def overlap(x1, y1, r1, x2, y2, r2):
            return (x2 - x1) ** 2 + (y2 - y1) ** 2 <= r2 ** 2
        for i, (x1, y1, r1) in enumerate(bombs):
            for j, (x2, y2, r2) in enumerate(bombs):
                if i != j and overlap(x2, y2, r2, x1, y1, r1):
                    graph[i].append(j) 
        def dfs(node, seen):
            exploded = 1
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    exploded += dfs(neighbor, seen)
            return exploded
        max_bomb = 0
        for i in range(len(bombs)):
            seen = set()
            seen.add(i)
            max_bomb = max(max_bomb, dfs(i, seen))

        return max_bomb

                



            

