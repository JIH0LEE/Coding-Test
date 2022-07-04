#백준
#24416
#알고리즘 수업-피보나치 수1
#pypy
n=int(input())
dp=[0]*(n+1)
cnt1=1
cnt2=0

def recursion(n):
    global cnt1
    if n==1 or n==2:
        return 1
    else:
        cnt1+=1
        return recursion(n-1)+recursion(n-2)

def dynamic(n):
    global cnt2
    dp[1],dp[2]=1,1
    for i in range(3,n+1):
        cnt2+=1
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

recursion(n)
dynamic(n)
print(cnt1,cnt2)
