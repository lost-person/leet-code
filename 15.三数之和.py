#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        
        nums.sort()
        
        def k_Sum(start: int, end: int, k: int, target: int):
            tmp_res = []
            if k == 2:
                while start < end:
                    tmp_sum = nums[start] + nums[end]
                    if tmp_sum == target:
                        tmp_res.append([nums[start], nums[end]])
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
                for i in range(start, len(nums) - k + 1):
                    if nums[i] * k > target:
                        break

                    if i == start or nums[i] != nums[i - 1]:
                        prev_tmp_res = k_Sum(i + 1, len(nums) - 1, k - 1, target - nums[i])
                        prev_tmp_res = [[nums[i]] + prev_tmp for prev_tmp in prev_tmp_res]
                        tmp_res.extend(prev_tmp_res)
            return tmp_res
        
        return k_Sum(0, len(nums) - 1, 3, 0)

# @lc code=end

