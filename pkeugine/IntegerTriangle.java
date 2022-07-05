import java.util.List;
import java.util.ArrayList;

// 프로그래머스
// 정수 삼각형
public class Main {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] input = {{7}, {3,8}, {8,1,0}, {2,7,4,4}, {4,5,2,6,5}};

        // 30
        System.out.println(solution.solution(input));
    }
}

class Solution {

    public int solution(int[][] triangle) {
        List<List<Integer>> results = new ArrayList<>();
        int triangleLength = triangle.length;

        List<Integer> firstResult = new ArrayList<>();
        firstResult.add(triangle[0][0]);
        if (triangleLength == 1) {
            return firstResult.get(0);
        }
        results.add(firstResult);

        for (int i = 1; i < triangleLength; i++) {
            List<Integer> currentResult = new ArrayList<>();
            List<Integer> beforeResult = results.get(i - 1);
            int[] triangleValue = triangle[i];
            int currentLength = triangleValue.length;

            for (int j = 0; j < currentLength; j++) {
                if (j == 0) {
                    currentResult.add(beforeResult.get(j) + triangleValue[0]);
                    continue;
                }
                if (j == currentLength - 1) {
                    currentResult.add(beforeResult.get(currentLength - 2) + triangleValue[currentLength - 1]);
                    continue;
                }
                currentResult.add(Math.max(
                            triangleValue[j] + beforeResult.get(j - 1),
                            triangleValue[j] + beforeResult.get(j)
                ));
            }

            results.add(currentResult);
        }

        int max = 0;
        List<Integer> lastResult = results.get(triangleLength - 1);
        for (int num : lastResult) {
            if (num > max) {
                max = num;
            }
        }
        return max;
    }
}


