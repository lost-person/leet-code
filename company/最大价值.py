# coding = utf-8

# 在n*n地图上，从左上角出发，每次沿着上下左右任意方向移动距离小于k，移动位置需要价值高于当前位置价值。
# 求路上的最大累计价值


def solve():
    n, k = map(int, input().split())
    matrix = []

    for i in range(n):
        matrix.append(list(map(int, input().split())))

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = [(0, 0, matrix[0][0])]
    max_fee = 0

    while queue:
        row, col, cur_fee = queue.pop()
        max_fee = max(max_fee, cur_fee)

        for direction in directions:
            next_row = row
            next_col = col
            for t in range(k):
                next_row = next_row + direction[0]
                next_col = next_col + direction[1]
                if 0 <= next_row < n and 0 <= next_col < n and matrix[row][
                        col] < matrix[next_row][next_col]:
                    queue.append((next_row, next_col,
                                  cur_fee + matrix[next_row][next_col]))

    return max_fee


solve()
