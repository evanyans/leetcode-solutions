class Solution:
    # Attempted 3/11/2025
    # AHA: to prevent rearrangement of the same answer, rememebr to
    # save where we are starting from, i.e. "start"
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(curr, total, seen, start):
            print(curr)
            if len(curr) == k and total == n:
                ans.append(curr[:])
                return
            for i in range(start, 10):
                if i in seen:
                    continue
                if len(curr) < k:
                    seen.add(i)
                    curr.append(i)
                    backtrack(curr, total + i, seen, i)
                    seen.remove(i)
                    curr.pop()
                

        ans = []
        backtrack([], 0, set(), 1)
        return ans
