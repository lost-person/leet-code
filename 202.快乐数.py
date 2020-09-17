#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#


# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 0:
            return False

        def get_next(cur_num: int):
            next_num = 0
            while cur_num > 0:
                cur_num, mod = divmod(cur_num, 10)
                next_num += mod**2
            return next_num

        slow, fast = n, get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1

        # ## 数学法
        # cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}

        # def get_next(number):
        #     total_sum = 0
        #     while number > 0:
        #         number, digit = divmod(number, 10)
        #         total_sum += digit ** 2
        #     return total_sum

        # while n != 1 and n not in cycle_members:
        #     n = get_next(n)

        # return n == 1


# @lc code=end
