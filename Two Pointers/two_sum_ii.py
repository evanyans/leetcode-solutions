class Solution:
    # Attempted 3/16/2025
    # AHA: easy, logical, if sum >, move right, if sum <, move left.
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # exactly one solution
        left = 0
        right = len(numbers) - 1
        while left < right:
            print(left, right)
            if (numbers[left] + numbers[right]) == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
        return 0
