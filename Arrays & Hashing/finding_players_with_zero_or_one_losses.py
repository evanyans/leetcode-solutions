class Solution:
    # Attempted 2/14/2025
    # AHA: happy valentines day <3. its just tracking but with a hashmap
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #answer[0] is a list of all players that have not lost any matches. returned in increasing
        #answer[1] is a list of all players that have lost exactly one match.
        loses = defaultdict(int)
        answer = [[], []]
        for arr in matches:
            loses[arr[0]] += 0
            loses[arr[1]] += 1
        
        for key in loses:
            if loses[key] == 0:
                answer[0].append(key)
            elif loses[key] == 1:
                answer[1].append(key)
        
        answer = [sorted(answer[0]), sorted(answer[1])]
        
        return answer
