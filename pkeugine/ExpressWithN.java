import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

// 프로그래머스
// N으로 표현
public class ExpressWithN {

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 4
        System.out.println(solution.solution(5, 12));
        // 3
        System.out.println(solution.solution(2, 11));
    }
}

class Solution {

    public int solution(int N, int number) {
        List<Set<Integer>> results = new ArrayList<>();

        int answer = 1;
        if (N == number) {
            return answer;
        }
        Set<Integer> oneResult = new HashSet<>();
        oneResult.add(N);
        results.add(oneResult);

        // answer = 2
        answer++;
        Set<Integer> twoResult = new HashSet<>();
        twoResult.add(N + N);
        twoResult.add(N * N);
        // N / N
        twoResult.add(1);
        // N - N
        twoResult.add(0);
        twoResult.add(Integer.valueOf(String.valueOf(N).repeat(2)));
        if (twoResult.contains(number)) {
            return answer;
        }
        results.add(twoResult);

        // answer 3 ~ 8
        while (answer < 8) {
            answer++;

            Set<Integer> result = new HashSet<>();
            for (int i = 0; i < answer - 1; i++) {
                Set<Integer> firstResult = results.get(i);
                Set<Integer> secondResult = results.get(answer - 2 - i);
                for (int first : firstResult) {
                    for (int second : secondResult) {
                        result.add(first + second);
                        result.add(first - second);
                        result.add(first * second);
                        if (first != 0 && second != 0) {
                            result.add(first / second);
                        }
                    }
                }
            }
            result.add(Integer.parseInt(String.valueOf(N).repeat(answer)));
            if (result.contains(number)) {
                return answer;
            }
            results.add(result);
        }
        return -1;
    }
}
