import sys

K, N = list(map(int, input().split()))
cables = [int(sys.stdin.readline()) for _ in range(K)]

left = 1
right = sum(cables) // K

while left <= right:
    mid = (left+right) // 2
    count = 0
    for length in cables:
        count += length // mid
        if count >= N:
            break

    if count >= N:
        left = mid + 1
    else:
        right = mid - 1
print(right)
