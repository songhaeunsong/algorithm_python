# 1926. 간단한 369게임

n = int(input())
result = []

for i in range(1, n+1):
    i = str(i)
    clap = 0
    for num in i:
        if num == "3" or num == "6" or num == "9":
            clap += 1

    result.append("-" * clap) if clap > 0 else result.append(i)


print(" ".join(result))