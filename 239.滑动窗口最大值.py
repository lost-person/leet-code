#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 当数组逆序时，退化为 O(n * k)
        # n = len(nums)
        # if not k or not n: return []

        # if k == 1: return nums

        # # 最大数及其索引
        # last_max, last_max_index = float('-inf'), -1
        # # 窗口的左右界
        # left, right = 0, k - 1

        # res = []
        # j = 0
        # while right < n:
        #     # 之前的最大值不在当前窗口内
        #     if last_max_index < left:
        #         last_max = float('-inf')
        #         for i in range(left, right + 1):
        #             if nums[i] > last_max:
        #                 last_max = nums[i]
        #                 last_max_index = i
        #     else:
        #         # 比较最新元素与之前的最大值
        #         if last_max < nums[right]:
        #             last_max = nums[right]
        #             last_max_index = right
        #     res.append(last_max)

        #     left += 1
        #     right += 1

        # return res

        # 双端队列
        # n = len(nums)
        # if n * k == 0:
        #     return []
        # if k == 1:
        #     return nums

        # def clean_deque(i):
        #     # remove indexes of elements not from sliding window
        #     if deq and deq[0] == i - k:
        #         deq.popleft()

        #     # remove from deq indexes of all elements
        #     # which are smaller than current element nums[i]
        #     while deq and nums[i] > nums[deq[-1]]:
        #         deq.pop()

        # # init deque and output
        # deq = deque()
        # max_idx = 0
        # for i in range(k):
        #     clean_deque(i)
        #     deq.append(i)
        #     # compute max in nums[:k]
        #     if nums[i] > nums[max_idx]:
        #         max_idx = i
        # output = [nums[max_idx]]

        # # build output
        # for i in range(k, n):
        #     clean_deque(i)
        #     deq.append(i)
        #     output.append(nums[deq[0]])
        # return output

        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        left = [0] * n
        left[0] = nums[0]
        right = [0] * n
        right[n - 1] = nums[n - 1]
        for i in range(1, n):
            # from left to right
            if i % k == 0:
                # block start
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
            # from right to left
            j = n - i - 1
            if (j + 1) % k == 0:
                # block end
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])

        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))

        return output


# @lc code=end
