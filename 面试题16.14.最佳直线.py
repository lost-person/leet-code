# coding = utf-8

from typing import List

class Solution:
    def bestLine(self, points: List[List[int]]) -> List[int]:
        res = [0, 0]
        max_point_num = 0

        n = len(points)
        for i in range(n - 1):
            for j in range(i + 1, n):
                cur_point_num = 2

                if n - j + 1 <= max_point_num: break

                x1 = points[j][0] - points[i][0]
                y1 = points[j][1] - points[i][1]

                for k in range(j + 1, n):
                    x2 = points[k][0] - points[i][0]
                    y2 = points[k][1] - points[i][1]
                
                    if x1 * y2 == x2 * y1:
                        cur_point_num += 1
                
                if cur_point_num > max_point_num:
                    max_point_num = cur_point_num
                    res[0] = i
                    res[1] = j

        return res