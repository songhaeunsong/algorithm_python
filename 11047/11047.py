# 동전 0

# 10 4200
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000

import sys
n, k = [*map(int, input().split())]
typesOfMoney = [int(sys.stdin.readline()) for _ in range(n)]

answer = 0;
for money in reversed(typesOfMoney):
    if k >= money:
        count = k // money
        answer += count
        k -= count * money
    if k == 0:
        print(answer)
        break

