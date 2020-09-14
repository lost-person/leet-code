#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        
        deadends = set(deadends)
        if target in deadends:
            return -1

        def bfs(cur_num):
            for i, n in enumerate(cur_num):
                n = int(n)
                for d in (-1, 1):
                    m = (n + d) % 10
                    yield cur_num[:i] + str(m) + cur_num[i + 1:]

        queue = deque([(start, 0)])
        seen = {start}
        while queue:
            cur_num, step = queue.popleft()
            
            if cur_num == target: return step
            if cur_num in deadends: continue
            
            step += 1
            for next_num in bfs(cur_num):
                if next_num not in seen:
                    seen.add(next_num)
                    queue.append((next_num, step))

        return -1
# @lc code=end

