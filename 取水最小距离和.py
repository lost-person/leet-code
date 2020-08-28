# coding = utf-8

# n户人家，选取一条和 Y 轴平行的小河，使得n户人家到小河的距离和最小。

n = int(input())

row_list = []
for _ in range(n):
    row, _ = map(int, input().split())
    row_list.append(row)

row_list.sort()

res = row_list[n // 2]
ans = 0
for i in range(n):
    ans += abs(res - row_list[i])

print(ans)
