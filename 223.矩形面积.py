#
# @lc app=leetcode.cn id=223 lang=python3
#
# [223] 矩形面积
#


# @lc code=start
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int,
                    G: int, H: int) -> int:
        area1 = abs((A - C) * (B - D))
        area2 = abs((E - G) * (F - H))

        def overlap_area(A: int, B: int, C: int, D: int, E: int, F: int,
                         G: int, H: int):
            if A > G or C < E or D < F or B > H:
                return 0
            x1 = max(A, E)
            x2 = min(C, G)
            y1 = max(B, F)
            y2 = min(D, H)
            return (y2 - y1) * (x2 - x1)

        return area1 + area2 - overlap_area(A, B, C, D, E, F, G, H)


# @lc code=end
