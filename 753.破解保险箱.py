#
# @lc app=leetcode.cn id=753 lang=python3
#
# [753] 破解保险箱
#

# @lc code=start
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        seen = set()
        ans = []
        def dfs(node):
            for x in map(str, range(k)):
                nei = node + x
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei[1:])
                    ans.append(x)

        dfs("0" * (n-1))
        return "".join(ans) + "0" * (n-1)

# @lc code=end

