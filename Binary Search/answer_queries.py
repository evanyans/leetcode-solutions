class Solution:
    # Attempted 3/26/2025
    # AHA: prefix sum + binary search to find insertion index. clever
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        print(prefix)
        ans = []
        for query in queries:
            left = 0
            right = len(prefix)
            while left < right:
                mid = (left + right) // 2
                if prefix[mid] > query:
                    right = mid
                else:
                    left = mid + 1
            ans.append(left)
        return ans
