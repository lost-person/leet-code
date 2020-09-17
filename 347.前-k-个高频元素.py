#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 直接排序 (略)
        # 大顶堆 (自己实现的见 295)
        cnt = Counter(nums)
        # return heapq.nlargest(k, cnt.keys(), key=cnt.get)

        buckets = [[] for _ in range(len(nums) + 1)]
        for x, y in cnt.items():
            buckets[y].append(x)
        res = []
        for i in range(len(nums), -1, -1):
            if len(res) > k:
                break
            res.extend(buckets[i])
        return res[:k]


# @lc code=end
