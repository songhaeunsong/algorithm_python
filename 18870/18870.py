# 좌표 압축

# 5
# 2 4 -10 4 -9

import sys

n = int(input())
coordinates = [*map(int, sys.stdin.readline().split())]
unique_coors = sorted(list(set(coordinates)))
answer = []

compression_map = {}
for i in range(len(unique_coors)):
    compression_map[unique_coors[i]] = i

answer = [str(compression_map[i]) for i in coordinates]
print(' '.join(answer))
