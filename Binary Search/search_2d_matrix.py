class Solution:
    # Attempted 4/22/2025
    # just binary search, learn matrix calculation
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                left = mid + 1
            elif matrix[row][col] > target:
                right = mid - 1
        return False
        
