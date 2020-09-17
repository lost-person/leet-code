#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        def k_sum(start: int, end: int, k: int, target):
            tmp_list = []
            if k == 2:
                while start < end:
                    tmp_sum = nums[start] + nums[end]
                    if tmp_sum == target:
                        tmp_list.append([nums[start], nums[end]])
                        while start < end and nums[start] == nums[start + 1]:
                            start += 1
                        while start < end and nums[end] == nums[end - 1]:
                            end -= 1
                        start += 1
                        end -= 1
                    elif tmp_sum < target:
                        start += 1
                    else:
                        end -= 1
            else:
                i = start
                while i < n - k + 1 and nums[i] * k <= target:
                    if i > start and nums[i] == nums[i - 1]:
                        i += 1
                        continue
                    tmp_res_list = k_sum(i + 1, n - 1, k - 1, target - nums[i])
                    for j in range(len(tmp_res_list)):
                        tmp_res_list[j] = [nums[i]] + tmp_res_list[j]
                    tmp_list.extend(tmp_res_list)
                    i += 1

            return tmp_list

        res = k_sum(0, n - 1, 4, target)
        return res


# @lc code=end
