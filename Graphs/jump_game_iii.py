class Solution:
    # Attempted 3/4/2025
    # AHA: tried both dfs and bfs, bfs probably makes more sense to reach true fastest, whereas dfs can reach unnecessary rabbit holes
    def canReach(self, arr: List[int], start: int) -> bool:
        # bfs soution:
        def valid(num): # check bounds
            return num < len(arr) and num >= 0
        graph = defaultdict(list)
        for i, n in enumerate(arr): # n represents jump length
            if valid(i - arr[i]):
                graph[i].append(i - arr[i]) # which indicies does index i link to
            if valid(i + arr[i]):
                graph[i].append(i + arr[i])   
        seen = set()
        seen.add(start)
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if arr[node] == 0:
                return True
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return False
          

        # DFS SOLUTION (FIRST ATTEMPT):

        # # - construct a graph using the jump lengths
        # # - dfs to 0
        # def valid(num): # check bounds
        #     return num < len(arr) and num >= 0
        # seen = set()
        # graph = defaultdict(list)
        # for i, n in enumerate(arr): # n represents jump length
        #     if valid(i - arr[i]):
        #         graph[i].append(i - arr[i]) # which indicies does index i link to
        #     if valid(i + arr[i]):
        #         graph[i].append(i + arr[i])
        # def dfs(node):
        #     if arr[node] == 0:
        #         return True
        #     for neighbor in graph[node]:
        #         if neighbor not in seen:
        #             seen.add(neighbor)
        #             if dfs(neighbor):
        #                 return True
        #     return False
        # return dfs(start)

