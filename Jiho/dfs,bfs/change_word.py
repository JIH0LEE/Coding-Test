#프로그래머스
#dfs,bfs
#단어 변환
from collections import deque
def check(a,b):
    n=len(a)
    rt=0
    for i in range(n):
        if a[i]!=b[i]:
            rt+=1
    return rt
def solution(begin, target, words):
    n=len(words)
    visited=[False for _ in range(n)]
    queue=deque([(begin,0)])
    answer = 0
    while queue:
        c,step=queue.popleft()

        if c==target:
            
            answer=step
            break
        for idx,word in enumerate(words):
            if not visited[idx]:
                
                if check(c,word)==1:
                    
                    visited[idx]=1
                    queue.append((word,step+1))
                

    return answer