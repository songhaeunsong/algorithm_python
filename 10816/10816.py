# 숫자 카드 2

# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10


import sys
input = sys.stdin.readline


n = int(input())
n_cards = [*map(int, input().split())]
m = int(input())
m_cards = [*map(int, input().split())]

card_map = {}
for card in n_cards:
    if card in card_map:
        card_map[card] += 1
    else:
        card_map[card] = 1

result = " ".join(str(card_map.get(type, 0)) for type in m_cards)
print(result)