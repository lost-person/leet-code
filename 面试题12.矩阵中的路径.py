# coding = utf-8
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        if not word:
            return True
        
        coordinates = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(board)
        n = len(board[0])
        
        def dfs(row, col, index):
            if index >= len(word):
                return True
            
            c = board[row][col]
            board[row][col] = '#'
            for coordinate in coordinates:
                new_row, new_col = row + coordinate[0], col + coordinate[1]
                if 0 <= new_row < m and 0 <= new_col < n and board[new_row][new_col] == word[index]:
                    if dfs(new_row, new_col, index + 1):
                        return True
            
            board[row][col] = c
            return False


        
        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:
                    if dfs(row, col, 1):
                        return True
        
        return False
