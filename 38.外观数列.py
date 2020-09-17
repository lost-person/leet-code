#
# @lc app=leetcode.cn id=38 lang=python3
# coding=utf-8
'''
@Author: lost-person
@Date: 2020-01-31 16:56:38
@Description: 
@LastEditTime : 2020-01-31 17:13:58
@FilePath: \leetcode\38.外观数列.py
'''

#
# [38] 外观数列
#


# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'

        i = 1
        prev_s = ''
        while i < n:
            cnt = 1
            for j in range(len(s) - 1):
                if s[j] == s[j + 1]:
                    cnt += 1
                else:
                    prev_s += str(cnt) + str(s[j])
                    cnt = 1
            prev_s += str(cnt) + str(s[len(s) - 1])
            s = prev_s
            prev_s = ''
            i += 1

        return s


# @lc code=end
