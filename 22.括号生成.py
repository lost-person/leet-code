#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [[] for i in range(n+1)]
        res[0] = [""]
 
        for i in range(1, n+1):
             for j in range(i):
                res[i] += ['('+k+')'+l for k in res[j] for l in res[i-j-1]]
        return res[n]
# @lc code=end

