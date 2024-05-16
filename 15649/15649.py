# 4 2

import sys
n, m = map(int, sys.stdin.readline().split())


def backtracking(arr, visited):

    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return

    for i in range(1, n+1):
        if visited[i] == 0:
            arr.append(i)
            visited[i] = 1
            backtracking(arr, visited)
            arr.pop()
            visited[i] = 0


backtracking([], [0] * (n+1))


