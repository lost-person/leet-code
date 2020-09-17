# coding = utf-8


class Solution:
    def isNumber(self, s: str) -> bool:
        if not s:
            return False

        n = len(s)

        def judge_p(index):
            """判断是否为指数
            """
            res = False
            for i in range(index, n):
                # 判断符号
                if s[i] == '+' or s[i] == '-':
                    if i != index:
                        return False
                # 判断是否为小数
                elif s[i] == '.':
                    return False
                elif s[i] < '0' and s[i] > '9':
                    return False
                else:
                    res = True
            return res

        def judge_s(index):
            """判断其他
            """
            point = False
            res = False
            for i in range(index):
                # 判断符号
                if s[i] == '+' or s[i] == '-':
                    if i != 0:
                        return False
                # 判断是否为小数
                elif s[i] == '.':
                    if not point:
                        point = True
                    else:
                        return False
                elif s[i] < '0' and s[i] > '9':
                    return False
                else:
                    res = True
            return res

        index = s.find('e')
        if index == -1:
            index = s.find('E')
            if index == -1:
                return judge_s(n)
            else:
                return judge_s(index) and judge_p(index + 1)
        else:
            return judge_s(index) and judge_p(index + 1)
