def solution(N, number):
    dp=[set() for _ in range(9)]
    dp[1]={N}
    answer = -1
    if N==number:
        answer=1
    else:
        tmp=N

        for i in range(2,9):
            tmp=tmp*10+N
            dp[i].add(tmp)
            for j in range(1,i):
                a=dp[j]
                b=dp[i-j]
                for elem in a:
                    for elem1 in b:
                        dp[i].add(elem+elem1)
                        dp[i].add(elem*elem1)
                        dp[i].add(elem-elem1)
                        dp[i].add(elem//elem1)
                        dp[i].add(elem1//elem)
            dp[i]=dp[i]-{0}
            if number in dp[i]:
                answer=i
                break

    
    return answer