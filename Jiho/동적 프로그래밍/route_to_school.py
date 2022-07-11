#프로그래머스
#동적 프로그래밍
#등굣길

def solution(m, n, puddles):
    dp=[[0 for i in range(m+1)] for j in range(n+1)]
    dp[1][1]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1:
                dp[i][j]=1
                continue
            if [j,i] not in puddles:
                print(1)
                dp[i][j]=(dp[i-1][j]+dp[i][j-1])%1000000007
    answer = dp[n][m]
    return answer