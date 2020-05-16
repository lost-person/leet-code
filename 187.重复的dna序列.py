#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # L, n = 10, len(s)
        # res = set()
        # if not s or n < L + 1:
        #     return list(res)
        
        # seen = set()
        # for i in range(n - L + 1):
        #     tmp = s[i: i + L]
        #     if tmp not in seen:
        #         seen.add(tmp[:])
        #     else:
        #         res.add(tmp[:])
        # return list(res)

        # # 利用 dna 序列最多包含4种元素的特点
        # L, n = 10, len(s)
        # if n <= L:
        #     return []
        
        # # rolling hash parameters: base a
        # a = 4
        # aL = pow(a, L) 
        
        # # convert string to array of integers
        # to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        # nums = [to_int.get(s[i]) for i in range(n)]
        
        # h = 0
        # seen, output = set(), set()
        # # iterate over all sequences of length L
        # for start in range(n - L + 1):
        #     # compute hash of the current sequence in O(1) time
        #     if start != 0:
        #         h = h * a - nums[start - 1] * aL + nums[start + L - 1]
        #     # compute hash of the first sequence in O(L) time
        #     else:
        #         for i in range(L):
        #             h = h * a + nums[i]
        #     # update output and hashset of seen sequences
        #     if h in seen:
        #         output.add(s[start:start + L])
        #     seen.add(h)
        # return output

        # 在上一种方法的基础上，将四进制转换为2进制
        L = 10
        if not s or len(s) < L + 1:
            return []

        n = len(s)
        seen, output = set(), set()
        to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [to_int[c] for c in s]

        start, bit_mask = 0, 0
        for start in range(n - L + 1):
            if start == 0:
                for i in range(L):
                    bit_mask <<= 2
                    bit_mask |= nums[i]
            else:
                bit_mask <<= 2
                bit_mask |= nums[start + L - 1]
                bit_mask &= ~(3 << 2 * L)
            
            if bit_mask in seen:
                output.add(s[start: start + L])
            else:
                seen.add(bit_mask)
        
        return list(output)
# @lc code=end

