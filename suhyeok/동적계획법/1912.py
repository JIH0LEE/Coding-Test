
# %%
n = int(input())

arr = [0 for i in range(n)]
arr = list(map(int, input().split()))
print(arr)

dp = [0 for i in range(n)]
dp[0] = arr[0]
for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i-1]+arr[i])

    # 밑의 식으로 했을 때는 Runtime Error 발생
    # 이유는 모르겠음!
    # dp_temp=dp[i-1]+arr[i]
    # dp[i]=max(arr[i],dp_temp)

print(max(dp))

# %%
