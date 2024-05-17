# 강의실 배정

# 3
# 1 3
# 2 4
# 3 5

import sys
n = int(input())

time_arr = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    time_arr.append([start, 1])
    time_arr.append([end, -1])

time_arr.sort(key=lambda x: (x[0], x[1]))

max_active = 0
active = 0
for time in time_arr:
    active += time[1]
    max_active = max(max_active, active)

print(max_active)
