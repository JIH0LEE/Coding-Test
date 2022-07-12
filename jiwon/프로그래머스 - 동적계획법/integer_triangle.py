def solution(triangle):
    dp = [triangle[-1]] # 맨 끝줄
    
    for i in range(len(triangle)-2, -1, -1):
        dp.append([])
        for j in range(len(triangle[i])):
            dp[-1].append(max(dp[-2][j], dp[-2][j+1])+triangle[i][j])
    return dp[-1][0]