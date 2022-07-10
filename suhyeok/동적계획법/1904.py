# 00이랑 1이니까
# dp[n]은 dp[n-1]+dp[n-1]인데 왜 그러냐면
# dp[n-2]는 뒤에 00이 들어가는 경우
# dp[n-1]은 뒤에 1이 들어가는 경우
n = int(input())

dp = [0 for i in range(1000001)]

dp[1] = 1
dp[2] = 2
# dp[3]=3
# dp[4]=5
for i in range(3, n+1):
    dp[i] = (dp[i-2]+dp[i-1]) % 15746

print(dp[n])
