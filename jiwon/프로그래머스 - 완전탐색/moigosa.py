#완전탐색 - 모의고사

def solution(answers):
    score_a, score_b, score_c = 0,0,0
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        s1 = i%len(a)
        s2 = i%len(b)
        s3 = i%len(c)
        
        if a[s1] == answers[i]:
            score_a+=1
        if b[s2] == answers[i]:
            score_b+=1
        if c[s3] == answers[i]:
            score_c+=1

    k = max(score_a, score_b, score_c)
    answer =[]
    
    if k == score_a:
        answer.append(1)
    if k == score_b:
        answer.append(2)
    if k == score_c:
        answer.append(3)
        
    return answer