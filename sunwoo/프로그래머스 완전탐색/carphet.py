def solution(brown, yellow):
    answer = []

    fpr col in range(3, brown//2):
        if(col-2)*(brown//2 - col)=yellow:
            return[brown//2-col+2, col]
