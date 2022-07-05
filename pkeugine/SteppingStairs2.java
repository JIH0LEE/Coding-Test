import java.util.Scanner;

// baekjun 2579
// 6
// 10 20 15 25 10 20
// answer: 75
public class SteppingStairs2 {

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution());
    }
}

class Solution {

    public int solution() {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] stairs = new int[n+1];

        for (int i = 1; i <= n; i++) {
            stairs[i] = sc.nextInt();
        }

        int[][] map = new int[n+1][2];
        map[1][0] = map[1][1] = stairs[1];
        for (int i = 2; i < n+1; i++) {
            map[i][0] = map[i-1][1] + stairs[i];
            map[i][1] = Math.max(map[i-2][0], map[i-2][1]) + stairs[i];
        }

        return Math.max(map[n][0], map[n][1]);
    }
}
