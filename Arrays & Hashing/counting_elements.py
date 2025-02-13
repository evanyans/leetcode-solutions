class Solution:
    # Attempted 2/12/2025
    # AHA: just preprocess with a set.
    def countElements(self, arr: List[int]) -> int:
        # count which elements have itself + 1 in the array
        my_set = set(arr)
        count = 0
        for i in range(len(arr)):
            if arr[i] + 1 in my_set:
                count += 1
                
        return count
