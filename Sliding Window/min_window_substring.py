class Solution:
    # Attempted 4/21/2025
    # AHA: not very hard, just the all keyword is new syntax for me
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        curr = Counter()
        t_counts = Counter(t)
        start = 0
        min_len = float('inf') #len(s)
        for right in range(len(s)):
            curr[s[right]] += 1
            # checking window condition
            while all(curr[c] >= t_counts[c] for c in t_counts):
            # try to shrink from the left
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left
                curr[s[left]] -= 1
                left += 1

        return s[start: start + min_len] if min_len != float('inf') else ""
        
