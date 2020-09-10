#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # if not heights: return 0
        # n = len(heights)
        # if n == 1: return heights[0]
        
        # area = 0
        # for i in range(n):
        #     minHeight = sys.maxsize
        #     for j in range(i, n):
        #         minHeight = min(minHeight, heights[j])
        #         area = max(area, minHeight * (j - i + 1))

        # def calculateArea(heights, left, right):
        #     if left > right:
        #         return 0
        #     minIndex = left
        #     for i in range(left + 1, right + 1):
        #         if heights[i] < heights[minIndex]:
        #             minIndex = i
        #     return max(heights[minIndex] * (right - left + 1), calculateArea(heights, left, right - 1), 
        #                 calculateArea(heights, left + 1, right))
        # return calculateArea(heights, 0, len(heights) - 1)
        
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            #print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res

# @lc code=end

