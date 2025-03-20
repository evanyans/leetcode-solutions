class Solution:
    # Attempted 3/19/2025
    # AHA: add and remove from the dictionary to avoid
    # recounting/reinitializing a dictionary
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
 
        left = 0
        window_count = Counter(s2[:len(s1)])
        s1_count = Counter(s1)
        if window_count == s1_count:
            return True

        for i in range(len(s1), len(s2)):
            window_count[s2[left]] -= 1
            left += 1
            window_count[s2[i]] += 1
            if window_count == s1_count:
                return True

        return False
            
