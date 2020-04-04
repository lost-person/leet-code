#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        res = 0
        if not commands:
            return res
        
        # 确定方向
        coordinate= [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0

        obstacles_set = set(map(tuple, obstacles))
        x, y = 0, 0
        res = 0
        for command in commands:
            if command > 0:
                # 更新坐标，判断是否有障碍物
                for step in range(command):
                    new_x = x + coordinate[direction][0]
                    new_y = y + coordinate[direction][1]
                    if (new_x, new_y) in obstacles_set:
                        break
                    x, y = new_x, new_y
                res = max(res, x ** 2 + y ** 2)
            # 更新方向
            elif command == -1:
                direction = (direction + 1) % 4
            elif command == -2:
                direction = (direction - 1) % 4
        
        return res
# @lc code=end

