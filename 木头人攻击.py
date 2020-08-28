# coding = utf-8

# n 轮攻击，m 个怪物，一次攻击b个怪物（一格血），每个怪物a血量，求消灭的怪物数

t = int(input())

for i in range(t):
    n, m, a, b = map(int, input().split())
    print(min(m, n * b // a))
