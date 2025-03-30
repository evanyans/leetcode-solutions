class Solution:
    # Attempted 3/30/2025
    # AHA: i cheated, think about a pingpong ball going up and down and up and down
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * numRows
        step = -1
        curr_row = 0
        for char in s:
            rows[curr_row] += char
            if curr_row == 0 or curr_row == numRows - 1:
                step = -step
            curr_row += step
        return ''.join(rows)


