# 2001. 파리 퇴치

# 2
# 5 2
# 1 3 3 6 7
# 8 13 9 12 8
# 4 16 11 12 6
# 2 4 1 23 2
# 9 13 4 7 3
# 6 3
# 29 21 26 9 5 8
# 21 19 8 0 21 19
# 9 24 2 11 4 24
# 19 29 1 0 21 19
# 10 29 6 18 4 3
# 29 11 15 3 3 29

T = int(input())
for test_case in range(T):
    n, m = map(int, input().split())
    graph = [[*map(int, input().split())] for _ in range(n)]

    prefix_sum = [[0] * (n+1) for _ in range(n+1)]
    for r in range(1, n+1):
        for c in range(1, n+1):
            prefix_sum[r][c] = graph[r-1][c-1] + prefix_sum[r-1][c] + prefix_sum[r][c-1] - prefix_sum[r-1][c-1]

    max_flies = 0
    for r in range(m, n+1):
        for c in range(m, n+1):
            target = prefix_sum[r][c] - prefix_sum[r][c-m] - prefix_sum[r-m][c] + prefix_sum[r-m][c-m]
            max_flies = max(max_flies, target)
    print(f"#{test_case} {max_flies}")