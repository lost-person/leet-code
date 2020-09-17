# coding = utf-8
class Solution:
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        if not s:
            return res

        for c in s:
            if c == ' ':
                res += '%20'
            else:
                res += c

        return res
