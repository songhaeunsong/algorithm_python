# 키로거

# 2
# <<BP<A>>Cd-
# ThIsIsS3Cr3t

import sys
n = int(input())


def decoding(code_str):
    left = []
    right = []

    for code in code_str:
        if code == "<":
            if len(left):
                right.append(left.pop())

        elif code == ">":
            if len(right):
                left.append(right.pop())

        elif code == "-":
            if len(left):
                left.pop()
        else:
            left.append(code)

    return left + right[::-1]


result = []

for _ in range(n):
    codes = str(sys.stdin.readline()).strip()
    decoded = decoding(codes)
    result.append("".join(decoded))

print("\n".join(result))