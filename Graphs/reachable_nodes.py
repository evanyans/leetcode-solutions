class Solution:
    # Attempted 3/2/2025
    # AHA: remember your graph construction dfs, and INITIALIZE THAT 0 NODE IN THE SET
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        no_set = set(restricted)
    
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        ans = 1
        seen = set([0])
        def dfs(node):
            nonlocal ans
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    if neighbor not in no_set:
                        ans += 1
                        print(neighbor)
                        dfs(neighbor)
                
        
        dfs(0)
        return ans
            
