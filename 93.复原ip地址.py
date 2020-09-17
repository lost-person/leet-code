#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#

# @lc code=start
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) < 4: return res

        def solve(s, tmp):
            if len(s) == 0 and len(tmp) == 4:
                res.append('.'.join(tmp))
                return

            if tmp and len(tmp) > 4:
                return

            for i in range(len(s)):
                # 添加新元素
                solve(s[i + 1:], tmp + [s[i]])
                # 拼接
                if tmp and tmp[-1] != '0' and int(tmp[-1] + s[i]) < 256:
                    tmp[-1] += s[i]
                    solve(s[i + 1:], tmp)
                return

        solve(s, [])
        return res


# @lc code=end
