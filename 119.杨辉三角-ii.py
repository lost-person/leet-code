#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # if rowIndex == 0: return [1]

        # prev_triangle = [1]
        # cur_triangle = []

        # for row_num in range(rowIndex):
        #     # The first and last row elements are always 1.
        #     cur_triangle = list(map(lambda x, y: x + y, [0] + prev_triangle, prev_triangle + [0]))
        #     prev_triangle = cur_triangle

        # return cur_triangle
        # result=[1]
        # def connect(rowIndex):
        #     for i in range(rowIndex):
        #         yield ((rowIndex-i)/(1+i))
        # num_default=1
        # important=connect(rowIndex)
        # for i in range(rowIndex):
        #     num_default *= next(important)
        #     result.append(round(num_default))
        # return result

        if rowIndex == 0:
            return [1]
    
        result = [0] * (rowIndex + 1)
        for index in range(rowIndex + 1):
            if index == 0:
                result[0] = 1
            elif index == 1:
                result[1] = rowIndex
            elif index <= rowIndex >> 1:
                result[index] = result[index - 1] * (rowIndex - index + 1) // index
            else:
                result[index] = result[rowIndex - index]
        
        return result
# @lc code=end

