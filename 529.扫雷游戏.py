#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#

# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        coordinate = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        m, n = len(board), len(board[0])

        def judge(board, row, col):
            """检查周围地雷数
            """
            cnt = 0
            for i in range(8):
                new_row = row + coordinate[i][0]
                new_col = col + coordinate[i][1]
                if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
                    continue
                if board[new_row][new_col] == 'M':
                    cnt += 1
            
            return cnt

        # def dfs(board, row, col):
        #     """dfs 更新
        #     """
        #     # 越界
        #     if row < 0 or row >= m or col < 0 or col >= n:
        #         return

        #     if board[row][col] == 'E':
        #         board[row][col] = 'B'
        #         cnt = judge(board, row, col)
        #         # 周围无地雷
        #         if not cnt:
        #             for i in range(8):
        #                 dfs(board, row + coordinate[i][0], col + coordinate[i][1])
        #         else:
        #             board[row][col] = str(cnt)
        #     elif board[row][col] == 'M':
        #         board[row][col] = 'X'

        # dfs(board, click[0], click[1])

        # bfs
        node_list = [(click[0], click[1])]
        while node_list:
            row, col = node_list.pop()
            if board[row][col] == 'E':
                board[row][col] = 'B'
                cnt = judge(board, row, col)
                if not cnt:
                    for i in range(8):
                        new_row = row + coordinate[i][0]
                        new_col = col + coordinate[i][1]
                        if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
                            continue
                        node_list.append((new_row, new_col))
                else:
                    board[row][col] = str(cnt)
            elif board[row][col] == 'M':
                board[row][col] = 'X'
        return board
# @lc code=end

