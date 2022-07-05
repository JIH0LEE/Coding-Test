import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 4
        System.out.println(solution.solution(5, 12));
        // 3
        //System.out.println(solution.solution(2, 11));
    }
}

class Solution {

    public int solution(int N, int number) {
        int answer = 0;
        List<Set<Integer>> possible = new ArrayList<>();

        while (answer < 8) {
            answer++;
            Set<Integer> results = new HashSet<>();
            if (answer == 1) {
                // case: number = N
                if (number == N) {
                    return answer;
                }

                results.add(N);
            }
            if (answer == 2) {
                int temp = N + N;
                if (temp == number) {
                    return answer;
                }
                results.add(temp);

                temp = N * N;
                if (temp == number) {
                    return answer;
                }
                results.add(temp);

                temp = 1;
                if (temp == number) {
                    return answer;
                }
                results.add(temp);

                temp = 0;
                if (temp == number) {
                    return answer;
                }
                results.add(temp);
            }
            if (answer > 2) {
                for (int i = 0; i <= answer; i++) {
                    Set<Integer> firstSet = possible.get(i);
                    Set<Integer> secondSet = possible.get(answer - i);

                    for (int first : firstSet) {
                        for (int second : secondSet) {
                            int temp = first + second;
                            if (temp == number) {
                                return answer;
                            }
                            results.add(temp);

                            temp = first - second;
                            if (temp == number) {
                                return answer;
                            }
                            results.add(temp);

                            temp = first * second;
                            if (temp == number) {
                                return answer;
                            }
                            results.add(temp);

                            if (first != 0 && second != 0) {
                                temp = first / second;
                                if (temp == number) {
                                    return answer;
                                }
                                results.add(temp);
                            }
                        }
                    }
                }
                results.add(Integer.valueOf(String.valueOf(N).repeat(answer)));
            }
            possible.add(results);
            answer++;
        }

        return -1;
    }
}
