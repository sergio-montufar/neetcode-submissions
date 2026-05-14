class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()


        def dfs(r, c, i):
            if i == len(word):
                return True
            if min(r, c) < 0 or r >= rows or c >= cols or board[r][c] != word[i] or (r, c) in visited:
                return False

            visited.add((r, c))
            if board[r][c] == word[i]:
                i += 1

            result = (dfs(r+1, c, i) or
                      dfs(r-1, c, i) or
                      dfs(r, c+1, i) or
                      dfs(r, c-1, i))
            visited.remove((r, c))
            return result


        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False
        


