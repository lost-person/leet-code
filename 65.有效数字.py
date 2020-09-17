#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#


# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        # # 去除首尾空格
        # s = s.strip()
        # if not s: return False

        # def judgeP(s):
        #     res = False
        #     pointed = False

        #     for i, c in enumerate(s):
        #         if c in ['+', '-']:
        #             if i != 0:
        #                 return False
        #         elif c == '.':
        #             if pointed: return False
        #             pointed = True
        #         elif c < '0' or c > '9': return False
        #         else: res = True
        #     return res

        # def judgeS(s):
        #     res = False

        #     for i, c in enumerate(s):
        #         if c in ['+', '-']:
        #             if i != 0:
        #                 return False
        #         elif c < '0' or c > '9': return False
        #         else: res = True
        #     return res

        # idx = s.find('e')
        # if idx == -1:
        #     return judgeP(s)
        # else:
        #     return judgeP(s[:idx]) and judgeS(s[idx + 1:])

        # DFA 太强了
        state = 0
        finals = 0b101101000
        transfer = [[0, 1, 6, 2, -1], [-1, -1, 6, 2, -1], [-1, -1, 3, -1, -1],
                    [8, -1, 3, -1, 4], [-1, 7, 5, -1, -1], [8, -1, 5, -1, -1],
                    [8, -1, 6, 3, 4], [-1, -1, 5, -1, -1], [8, -1, -1, -1, -1]]

        def make(c):
            if c == ' ': return 0
            elif c in ['+', '-']: return 1
            elif c == '.': return 3
            elif c == 'e': return 4
            elif c >= '0' and c <= '9': return 2
            else: return -1

        for c in s:
            idx = make(c)
            if idx < 0: return False
            state = transfer[state][idx]
            if state < 0: return False

        return (finals & (1 << state)) > 0


# @lc code=end
