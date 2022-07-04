#백준
#2579
#계단 오르기
#pypy

import sys
input = sys.stdin.readline
n = int(input())
cost = [0]
dp = []
for i in range(n):
    cost.append(int(input()))

for i in range(n+1):
    if i == 0:
        dp.append(0)
    elif i == 1:
        dp.append(cost[i])
    elif i == 2:
        dp.append(dp[i-1]+cost[i])
    else:
        dp.append(max(dp[i-2]+cost[i], dp[i-3]+cost[i-1]+cost[i]))

print(dp[n])