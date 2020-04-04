# coding = utf-8

class Solution:
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if not a:
            return b

        # (n & 0xffffffff)进行这种变换的原因是,如果存在负数则需要转换成补码的形式,正数补码是他本身
        a &= 0xffffffff#
        b &= 0xffffffff

        while b != 0:
            carry = ((a & b) << 1) & 0xffffffff#如果是负数,转换成补码形式
            a ^= b
            b = carry
        
        if a < 0x80000000:#如果是正数的话直接返回
            return a
        else:
            return ~(a^0xffffffff)#是负数的话,转化成其原码
