class Solution:
    # Attempted 5/15/2025
    # AHA moment: Once our length of visited is equal to the len of rooms
    # we have visited all rooms, i.e. check if we visited all rooms
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # n rooms
        # labeled 0, n - 1 (indicies means the room number)
        # all the rooms are locked except for room 0
        # Each room has a key with a number on it

        # START AT ROOM 0
        # [[1, 3], [3, 0, 1], [2], [0]]
    
        # room_visited = 1
        # dfs(1) 
        #   room_visited++
        #   dfs(3), {dfs(0), dfs(1) is not ran because 1 in seen}
        #   dfs(0) not ran because already in seen
        # dfs(3)
        #   room_visited++
        #   dfs(0) not ran because already in seen

        graph = defaultdict(list)
        room_counter = len(rooms)

        visited = set()
        visited.add(0) # We visit 0 first, so add 0 to our visited set
        for i in range(len(rooms)):
            for key in rooms[i]:
                graph[i].append(key)

        # Given that we start at room 0

        # current bug: each key can contribute to true/false
        def dfs(room_num):
            # Iterate through every key of room_num and dfs it
            print(len(visited), room_counter)
            if len(visited) == room_counter:
                return True
            for key in rooms[room_num]:
                if key not in visited:
                    visited.add(key)
                    if dfs(key):
                        return True
            return False

        return dfs(0)




        
            

