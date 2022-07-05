import java.util.ArrayList;
import java.util.List;

// 프로그래머스
// 모의고사
public class Moigosa {

    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] firstInput = {1,2,3,4,5};
        int[] firstAnswer = sol.solution(firstInput);

        int[] secondInput = {1,3,2,4,2};
        int[] secondAnswer = sol.solution(secondInput);

        System.out.println("first answer");
        for (int i = 0; i < firstAnswer.length; i++) {
            System.out.println(firstAnswer[i]);
        }

        System.out.println("second answer");
        for (int i = 0; i < secondAnswer.length; i++) {
            System.out.println(secondAnswer[i]);
        }
    }
}

class Solution {

    public int[] solution(int[] answers) {
        int[] a = {1, 2, 3, 4, 5};
        int[] b = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] c = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] score = new int[3];

        int answersLength = answers.length;
        int aLength = a.length;
        int bLength = b.length;
        int cLength = c.length;
        for (int i = 0; i < answersLength; i++) {
            if (answers[i] == a[i%aLength]) {
                score[0]++;
            }
            if (answers[i] == b[i%bLength]) {
                score[1]++;
            }
            if (answers[i] == c[i%cLength]) {
                score[2]++;
            }
        }

        List<Integer> answerList = new ArrayList<>();
        int maxScore = Math.max(Math.max(score[0], score[1]), score[2]);
        if (maxScore == score[0]) {
            answerList.add(1);
        }
        if (maxScore == score[1]) {
            answerList.add(2);
        }
        if (maxScore == score[2]) {
            answerList.add(3);
        }

        int answerSize = answerList.size();
        int[] answer = new int[answerSize];
        for (int i = 0; i < answerSize; i++) {
            answer[i] = answerList.get(i);
        }
        return answer;
    }
}
