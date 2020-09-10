#
# @lc app=leetcode.cn id=301 lang=python3
#
# [301] 删除无效的括号
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return [""]
        
        def isValid(s:str)->bool:
            cnt = 0
            for c in s:
                if c == "(": cnt += 1
                elif c == ")": cnt -= 1
                if cnt < 0: return False  # 只用中途cnt出现了负值，你就要终止循环，已经出现非法字符了
            return cnt == 0

        # BFS
        level = {s}  # 用set避免重复
        while True:
            valid = list(filter(isValid, level))  # 所有合法字符都筛选出来
            if valid: return valid # 如果当前valid是非空的，说明已经有合法的产生了
            # 下一层level
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in "()":                     # 如果item[i]这个char是个括号就删了，如果不是括号就留着
                        next_level.add(item[:i]+item[i+1:])
            level = next_level

        # left_rem, right_rem = 0, 0
        # for c in s:
        #     if c == '(':
        #         left_rem += 1
        #     elif c == ')':
        #         right_rem = right_rem + 1 if left_rem == 0 else right_rem
        #         left_rem = left_rem - 1 if left_rem > 0 else left_rem
        
        # res = {}
        # def recurse(index, left_cnt, right_cnt, left_rem, right_rem, expr):
        #     if index == len(s):
        #         if not (left_rem or right_rem):
        #             ans = ''.join(expr)
        #             res[ans] = 1
        #     else:
        #         if (s[index] == '(' and left_rem > 0) or (s[index] == ')' and right_rem > 0):
        #             recurse(index + 1, left_cnt, right_cnt, left_rem - (s[index] == '('), 
        #             right_rem - (s[index] == ')'), expr)
                
        #         expr.append(s[index])

        #         if s[index] != '(' and s[index] != ')':
        #             recurse(index + 1, left_cnt, right_cnt, left_rem, right_rem, expr)
        #         elif s[index] == '(':
        #             recurse(index + 1, left_cnt + 1, right_cnt, left_rem, right_rem, expr)
        #         elif s[index] == ')' and left_cnt > right_cnt:
        #             recurse(index + 1, left_cnt, right_cnt + 1, left_rem, right_rem, expr)
                
        #         expr.pop()
        
        # recurse(0, 0, 0, left_rem, right_rem, [])
        # return list(res.keys())
# @lc code=end

