// 프로그래머스
// 카펫
public class Carpet {

    public static void main(String[] args) {
        Solution solution = new Solution();

        // [4,3]
        int[] first = solution.solution(10, 2);
        for (int num : first) {
            System.out.println(num);
        }
        System.out.println();

        // [3,3]
        int[] second = solution.solution(8, 1);
        for (int num : second) {
            System.out.println(num);
        }
        System.out.println();

        // [8,6]
        int[] third = solution.solution(24, 24);
        for (int num : third) {
            System.out.println(num);
        }
        System.out.println();
    }
}

class Solution {

    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        boolean notFinished = true;
        int m = 3;

        while (notFinished) {
            for (int n = m; n >= 3; n--) {
                if (isCarpet(m, n, brown, yellow)) {
                    answer[0] = m;
                    answer[1] = n;
                    notFinished = false;
                }
            }
            m++;
        }

        return answer;
    }

    private boolean isCarpet(int m, int n, int brown, int yellow) {
        return validateBrown(m, n, brown) && validateYellow(m, n, yellow);
    }

    private boolean validateBrown(int m, int n, int brown) {
        return brown == (2 * m) + (2 * n) - 4;
    }

    private boolean validateYellow(int m, int n, int yellow) {
        return yellow == (m - 2) * (n - 2);
    }
}
