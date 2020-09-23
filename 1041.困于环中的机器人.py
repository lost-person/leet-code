#
# @lc app=leetcode.cn id=1041 lang=python3
#
# [1041] 困于环中的机器人
#

# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        if not instructions: return False

        direction = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        for ins in instructions:
            if ins == "R":
                direction += 1
            elif ins == "L":
                direction += 3
            else:
                direction = direction % 4
                x += directions[direction][0]
                y += directions[direction][1]
        
        return (x == y == 0) or (direction % 4 != 0)
# @lc code=end

