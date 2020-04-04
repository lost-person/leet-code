#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.data = []
    #     self.min_index = 0

    # def push(self, x: int) -> None:
    #     self.data.append(x)
    #     if self.data[self.min_index] > x:
    #         self.min_index = len(self.data) - 1

    # def pop(self) -> None:
    #     self.data.pop()
    #     if self.min_index != len(self.data):
    #         return
    #     self.arrange()

    # def top(self) -> int:
    #     return self.data[-1]

    # def getMin(self) -> int:
    #     if len(self.data) < 0:
    #         return None
    #     return self.data[self.min_index]

    # def arrange(self) -> None:
    #     if len(self.data) <= 0:
    #         return
    #     min_index = 0
    #     for i in range(len(self.data)):
    #         if self.data[i] < self.data[min_index]:
    #             min_index = i
    #     self.min_index = min_index

    def __init__(self):
        # 数据栈
        self.data = []
        # 辅助栈
        self.helper = []

    def push(self, x):
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self):
        if self.data:
            self.helper.pop()
            return self.data.pop()

    def top(self):
        if self.data:
            return self.data[-1]

    def getMin(self):
        if self.helper:
            return self.helper[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

