import sys

input = list(map(int, sys.stdin.readline().split()))

A = input[0]
B = input[1]
C = input[2]

if B >= C:
    print(-1)

else:
    N = C-B
    answer = int(A//N+1)
    print(answer)
