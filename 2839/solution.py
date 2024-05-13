# 설탕 배달

def countBag(N):
    if N % 5 == 0:
        return N//5
    countThree = 0
    while N > 0:
        N -= 3
        countThree += 1
        if N % 5 == 0 :
            return countThree + N//5
    return countThree if N == 0 else -1


N = int(input())
print(countBag(N))