class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        up, down, = 0, rows - 1

        while up <= down:
            row = (up + down) // 2
            if target > matrix[row][-1]:
                up = row + 1
            elif target < matrix[row][0]:
                down = row - 1
            else:
                break
        
        if not (up <= down):
            return False

        row = (up + down) // 2
        l, r = 0, cols - 1
        while l <= r:
            col = (l + r) // 2
            if target > matrix[row][col]:
                l = col + 1
            elif target < matrix[row][col]:
                r = col - 1
            else:
                return True
        
        return False


