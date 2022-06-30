def solution(answers):
    answer = []

    # 1번 학생
    student_answer1 = [1, 2, 3, 4, 5]
    # 2번 학생
    student_answer2 = [2, 1, 2, 3, 2, 4, 2, 5]
    # 3번 학생
    student_answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 학생들 맞은 갯수 세는 배열
    cnt = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == student_answer1[i % len(student_answer1)]:
            cnt[0] += 1
        if answers[i] == student_answer2[i % len(student_answer2)]:
            cnt[1] += 1
        if answers[i] == student_answer3[i % len(student_answer3)]:
            cnt[2] += 1

    max_score = max(cnt)

    for i in range(0, 3):
        if max_score == cnt[i]:
            answer.append(i+1)

    return answer
