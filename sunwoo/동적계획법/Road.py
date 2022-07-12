def solution(m, n, puddles):
    mapp = [[0] * (m+1) for _ in range(n+1)]
    
    mapp[1][1] = 1
    
    for x in range(1, n+1):
        for y in range(1, m+1):
            if x == 1 and y == 1:
                continue
                
            if [y, x] in puddles:
                mapp[x][y] = 0
            else:
                mapp[x][y] = mapp[x-1][y] + mapp[x][y-1]
    
    return mapp[-1][-1] % 1000000007
  
  
  
  
  '''
오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성
'''
