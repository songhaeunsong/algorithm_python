# 1로 만들기

target = 10
dp = [0] * (target + 1)
dp[1] = 0


def search(n):
    for i in range(2, n+1):
        minCount = dp[i - 1]

        if i % 2 == 0:
            minCount = min(minCount, dp[i//2])
        if i % 3 == 0:
            minCount = min(minCount, dp[i//3])

        dp[i] = minCount + 1
    return dp[n]


result = search(target)
print(result)

