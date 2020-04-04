#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        last_gas = 0

        n = len(gas)

        start = 0
        step = 0

        while start < n:
            cur_index = (start + step) % n
            last_gas = gas[cur_index] + last_gas - cost[cur_index]
            if last_gas < 0:
                start += 1
                step = 0
                last_gas = 0
                continue
            else:
                step += 1
            if step == n:
                return start
        
        return -1
# @lc code=end

