#
# @lc app=leetcode.cn id=825 lang=python3
#
# [825] 适龄的朋友
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        res = 0
        if not ages or len(ages) < 2: return res

        count = [0] * 121
        for age in ages:
            count[age] += 1

        for age_a, cnt_a in enumerate(count):
            for age_b, cnt_b in enumerate(count):
                if age_a * 0.5 + 7 >= age_b: continue
                if age_a < age_b: continue
                if age_a < 100 < age_b: continue
                res += cnt_a * cnt_b
                if age_a == age_b: res -= cnt_a

        return res


# @lc code=end
