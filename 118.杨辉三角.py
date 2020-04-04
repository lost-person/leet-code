#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # if not numRows: return []
        # if numRows == 1: return [[1]]

        # res = [[1]]
        # for i in range(1, numRows):
        #     tmp1 = []
        #     tmp2 = [0] + res[i - 1] + [0]
        #     for j in range(0, len(tmp2) - 1, 1):
        #         tmp1.append(tmp2[j] + tmp2[j + 1])
        #     res.append(tmp1[:])
        
        # return res

        triangle = []

        for row_num in range(numRows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle
# @lc code=end

