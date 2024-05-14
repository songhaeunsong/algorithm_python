# 1, 2, 3 더하기

# 3
# 4
# 7
# 10

import sys
input = sys.stdin.readline

n = int(input())

dp = [1] * 11
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]


result = ""
for _ in range(n):
    target = int(input())
    result += str(dp[target]) + "\n"

print(result.strip())
