public class Network {

    // 프로그래머스
    // 네트워크
    public static void main(String[] args) {
        Solution solution = new Solution();

        // 2
        int firstN = 3;
        int[][] firstComputers = {{1,1,0}, {1,1,0}, {0,0,1}};
        System.out.println(solution.solution(firstN, firstComputers));

        // 1
        int secondN = 3;
        int[][] secondComputers = {{1,1,0}, {1,1,1}, {0,1,1}};
        System.out.println(solution.solution(secondN, secondComputers));
    }
}

class Solution {

  public int solution(int n, int[][] computers) {
    int answer = 0;
    boolean[] check = new boolean[n];

    for (int i = 0; i < n; i++) {
      if (!check[i]) {
        dfs(computers, i, check);
        answer++;
      }
    }

    return answer;
  }

  private boolean[] dfs(int[][] computers, int i, boolean[] check) {
    check[i] = true;

    for (int j = 0; j < computers.length; j++) {
      if (i != j && computers[i][j] == 1 && check[j] == false) {
        check = dfs(computers, j, check);
      }
    }
    return check;
  }
}
