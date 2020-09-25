#
# @lc app=leetcode.cn id=901 lang=python3
#
# [901] 股票价格跨度
#


# @lc code=start
class StockSpanner:
    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        weight = 1
        while self.prices and self.prices[-1][0] <= price:
            weight += self.prices.pop()[-1]
        self.prices.append((price, weight))

        return weight


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end
