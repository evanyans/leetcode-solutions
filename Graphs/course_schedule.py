class Solution:
    # Attempted 3/17/2025
    # AHA: use indegree, kahns algorithm?
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build a prerequisite graph
        graph = defaultdict(list)

        # indegree represents number of prerequisites
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        # graph[b] -> all the courses you can take with prerequisite b
        # idea is: keep bfs graph[b] to see if we hit a depth >= numCourses
        
        # we should iterate starting from all courses
        # that has no prerequisite
        queue = deque([])
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        depth = 0
        while queue:
            node = queue.popleft()
            depth += 1
            if depth >= numCourses:
                return True
            for neighbor in graph[node]:
                # we have taken the course, so now remove
                # the prerequisite, i.e. the in_degree
                in_degree[neighbor] -= 1
                # if out of prerequisites, we can now take the course
                # i.e. add to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return False






        
        
