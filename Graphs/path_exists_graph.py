class Solution:
  # Attempted 2/28/2025
  # AHA: probably not the fastest, fastest requires queue, I used dfs basic
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # bi-directional just means undirected graph
        # given edges[i] = [u_i, v_i]: array of edges, thus build undirected graph
        if not edges:
            return True
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x) # necessary for undirected

        seen = set()

        def dfs(node):
            if node == destination:
                return True
            
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    if dfs(neighbor):
                        return True
            return False
        return dfs(source)




        
