# ATM

N = int(input())
times = list(map(int, input().split()))
times.sort()

sum = 0
for i in range(len(times)):
    sum += times[i] * (N-i)


print(sum)