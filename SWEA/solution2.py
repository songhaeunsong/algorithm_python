# 1859. 백만 장자 프로젝트

# 3
# 3
# 10 7 6
# 3
# 3 5 9
# 5
# 1 1 3 1 2

T = int(input())

for test_case in range(1, T+1):

    n = int(input())
    price = [*map(int,input().split())]

    profit_sum = 0
    max_price = 0

    for i in range(n - 1, -1, -1):
        if price[i] > max_price:
            max_price = price[i]
        profit_sum += max_price - price[i]

    print(f"#{test_case} {profit_sum}")

