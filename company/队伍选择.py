# coding = utf-8

# n个人，任意选取几个人作为一个团队，并从中选取队长，求方案数。队长不同，人不同都是不同的选择。

# \sum_{i=1}^n i * C_n^i = n * 2 ** (n - 1)

n = int(input())

def quick_mod(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    
    res = quick_mod(n // 2)
    if n & 1 == 0:
        return (res * res) % (10 ** 9 + 7)
    else:
        return 2 * ((res * res) % (10 ** 9 + 7)) % 10 ** 9 + 7

total_num = quick_mod(n * quick_mod(n - 1))
print(total_num)
