import java.util.*;

// 프로그래머스
// 소수 찾기
public class FindPrime {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String input = "17";
        String second = "011";
        System.out.println(solution.solution(input));
        System.out.println();
        System.out.println(solution.solution(second));
    }
}

class Solution {

    private boolean[] visited;
    private Set<Integer> answers;

    public int solution(String numbers) {
        visited = new boolean[numbers.length()];
        answers = new HashSet<>();
        findPrime(0, numbers, "");
        return answers.size();
    }

    private void findPrime(int depth, String numbers, String previous) {
        int numbersLength = numbers.length();
        if (depth == numbersLength) {
            return;
        }

        for (int i = 0; i < numbersLength; i++) {
            if (!visited[i]) {
                visited[i] = true;

                String currentString = previous + numbers.charAt(i);
                int current = Integer.parseInt(currentString);
                if (isPrime(current)) {
                    answers.add(current);
                }

                findPrime(depth + 1, numbers, currentString);

                visited[i] = false;
            }
        }
    }

    private boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }

        for (int i = 2; i < number; i++) {
            if (number % i == 0) {
                return false;
            }
        }

        return true;
    }
}
