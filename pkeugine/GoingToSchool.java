// 프로그래머스
// 등굣길
public class GoingToSchool {

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 4
        int[][] puddles = {{2,2}};
        System.out.println(solution.solution(4, 3, puddles));
    }
}

class Solution {

    public int solution(int m, int n, int[][] puddles) {
        int[][] possible = new int[m+1][n+1];

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (i == 1 && j == 1) {
                    possible[i][j] = 1;
                    continue;
                }
                possible[i][j] = (possible[i-1][j] + possible[i][j-1]) % 1000000007;
                for (int[] puddle : puddles) {
                    if (puddle[0] == i && puddle[1] == j) {
                        possible[i][j] = 0;
                        break;
                    }
                }
            }
        }

        return possible[m][n];
    }
}
