#
# @lc app=leetcode.cn id=900 lang=python3
#
# [900] RLE 迭代器
#

# @lc code=start

from typing import List
import bisect

class RLEIterator:

    def __init__(self, A: List[int]):
        self.rle = []
        
        i = 0
        n = len(A)
        
        left = 1
        for i in range(0, n, 2):
            if A[i] == 0: continue

            self.rle.append((left, left + A[i] - 1, A[i + 1]))
            left += A[i]
        
        self.cnt = 0
        self.boundary = []

        for i in range(len(self.rle)):
            self.boundary.append(self.rle[i][1])

    def next(self, n: int) -> int:
        self.cnt += n
        if self.cnt > self.boundary[-1]:
            return -1
        
        index = bisect.bisect_left(self.boundary, self.cnt)
        return self.rle[index][2]


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
# @lc code=end

