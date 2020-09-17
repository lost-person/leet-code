# coding = utf-8

from typing import List


class Solution:
    def twoSum(self, n: int) -> List[float]:
        res = []
        if not n:
            return res

        dp = [0] * (n * 6 + 1)
        for i in range(1, 7):
            dp[i] = 1

        for i in range(2, n + 1):
            for j in range(6 * i, i - 1, -1):
                dp[j] = 0
                for cur in range(1, 7):
                    if j - cur < i - 1:
                        break
                    dp[j] += dp[j - cur]

        all_cnt = sum(dp[n:n * 6 + 1])
        for i in range(n, n * 6 + 1):
            res.append(dp[i] / all_cnt)
        return res
