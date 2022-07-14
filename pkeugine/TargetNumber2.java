public class TargetNumber2 {

    // 프로그래머스
    // 타겟 넘버 풀이 2
    public static void main(String[] args) {
        Solution solution = new Solution();

        // 5
        int[] firstNumbers = {1,1,1,1,1};
        int firstTarget = 3;
        System.out.println(solution.solution(firstNumbers, firstTarget));

        // 2
        int[] secondNumbers = {4,1,2,1};
        int secondTarget = 4;
        System.out.println(solution.solution(secondNumbers, secondTarget));
    }
}

class Solution {

    public int solution(int[] numbers, int target) {
        return dfs(numbers, 0, target, 0);
    }

    private int dfs(int[] numbers, int depth, int target, int previous) {
        if (depth == numbers.length) {
            if (target == previous) {
                return 1;
            }
            return 0;
        } else {
            return dfs(numbers, depth + 1, target, previous + numbers[depth])
                + dfs(numbers, depth + 1, target, previous - numbers[depth]);
        }
    }
}
