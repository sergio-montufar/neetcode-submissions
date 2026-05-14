class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        rows, cols = len(board), len(board[0])

        def dfs(x, y, i): #backtrack
            if i == len(word):
                return True

            if x < 0 or x >= rows or y < 0 or y >= cols or (x, y) in visited or board[x][y] != word[i]:
                return False

            # i += 1
            visited.add((x, y))
            result = (dfs(x+1, y, i+1) or
                     dfs(x-1, y, i+1) or
                     dfs(x, y+1, i+1) or
                     dfs(x, y-1, i+1))
            visited.remove((x, y))
            return result


        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False