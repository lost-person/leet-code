#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if not nums or len(nums) < 2: return False     
        if k < 0 or t < 0: return False
        
        bucket = dict()

        def get_id(num, w):
            """计算桶id
            """
            return (num + 1) // w - 1 if num < 0 else num // w
        
        w = t + 1

        for i, num in enumerate(nums):
            bucket_id = get_id(num, w)
            
            # 当前桶
            if bucket_id in bucket:
                return True
            # 前一桶
            elif (bucket_id - 1) in bucket and abs(num - bucket.get(bucket_id - 1)) < w:
                return True
            # 后一桶
            elif (bucket_id + 1) in bucket and abs(num - bucket.get(bucket_id + 1)) < w:
                return True
            
            bucket[bucket_id] = num
            if i >= k: 
                bucket.pop(get_id(nums[i - k], w))

        return False
# @lc code=end

