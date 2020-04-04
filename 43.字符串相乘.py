#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # res = 0
        # if num1 == "0" or num2 == "0": return str(res)
        
        # num1 = num1[::-1]
        # num2 = num2[::-1]

        # carry = 1
        # num1_list = []
        # num2_list = []
        
        # for n1 in num1:
        #     num1_list.append(int(n1) * carry)
        #     carry *= 10
        
        # carry = 1
        # for n2 in num2:
        #     num2_list.append(int(n2) * carry)
        #     carry *= 10
        
        # for n1 in num1_list:
        #     for n2 in num2_list:
        #         res += n1 * n2
        # return str(res)

        n1 = len(num1)
        n2 = len(num2)
        if not (n1 or n2): return ""
        if num1 == "0" or num2 == "0": return "0"
        
        mul = [0 for _ in range(n1 + n2)]

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                bitmul = int(num1[i]) * int(num2[j])
                bitmul += mul[i + j + 1]
                mul[i + j] += bitmul // 10
                mul[i + j + 1] = bitmul % 10
        
        mul = list(map(lambda x: str(x), mul))
        i = 0
        while True:
            if mul[i] != "0":
                break
            i += 1
        return ''.join(mul[i:])
# @lc code=end

