# coding = utf-8

# 输入一个数字串，可在数字串之间添加 +/-，判断最终是否等于目标值。

row = int(input())


def backtrack(num: str, cur_sum: int, target: int, res: int, visited: set):
    if not num:
        if target == cur_sum:
            return True
        return False

    for next_sum in (cur_sum + int(num[0]), cur_sum - int(num[0]),
                     cur_sum * 10 + int(num[0])):
        if (next_sum, len(num[1:])) in visited:
            res += 1
        else:
            if backtrack(num[1:], next_sum, target, res, visited):
                res += 1
                visited.add((next_sum, len(num[1:])))

    return res


visited = set()
for i in range(row):
    num, target = input().split()
    target = int(target)
    print(backtrack(num[1:], int(num[0]), target, 0, visited))
    visited.clear()
