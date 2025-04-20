class Solution:
    #  Attempted 4/20/2025
    # AHA: same as course schedule 1, but change how you return the answer
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        in_degree = [0] * numCourses
        # in degree represents number of prerequisites
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        # graph[b]: all the courses you can take with prequisite b
        
        # We will start queue with all the courses that have no prerequisites
        queue = deque([])
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        depth = 0
        ans = []
        completed = False
        while queue:
            node = queue.popleft()
            depth += 1
            ans.append(node)
            if depth >= numCourses:
                completed = True
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return ans if completed else []
        
