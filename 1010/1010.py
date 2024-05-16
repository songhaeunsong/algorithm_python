# 다리 놓기

import sys
n = int(input())
dp = [[0] * 30 for _ in range(30)]


for i in range(1, 30):
    dp[1][i] = i
    dp[i][i] = 1

for i in range(2, 30):
    for j in range(2, 30):
        dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

for _ in range(n):
    start, end = [*map(int, sys.stdin.readline().split())]
    print(dp[start][end])

