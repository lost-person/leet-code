#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens: return 0

        stack = []
        for token in tokens:
            if token not in '+-*/':
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                if token == '+':
                    res = b + a
                elif token == '-':
                    res = b - a
                elif token == '*':
                    res = b * a
                else:
                    res = int(b / a)
                stack.append(res)
        
        return stack[0]
# @lc code=end

