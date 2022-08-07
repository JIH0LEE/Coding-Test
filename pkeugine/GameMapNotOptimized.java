public class GameMapNotOptimized {

    // 프로그래머스
    // 게임 맵 최단거리
    public static void main(String[] args) {
        Solution solution = new Solution();

        // 11
        int[][] firstMaps = {{1,0,1,1,1}, {1,0,1,0,1}, {1,0,1,1,1}, {1,1,1,0,1}, {0,0,0,0,1}};
        System.out.println(solution.solution(firstMaps));
        // -1
        int[][] secondMaps = {{1,0,1,1,1}, {1,0,1,0,1}, {1,0,1,1,1}, {1,1,1,0,0}, {0,0,0,0,1}};
        System.out.println(solution.solution(secondMaps));
    }
}

class Solution {

    private boolean[][] visited;

    // 상대팀 진영은 항상 배열의 가장 마지막 부분인가...?
    public int solution(int[][] maps) {
        visited = new boolean[maps.length][maps[0].length];
        // 지나가는 칸의 개수를 세야하므로 첫 시작부터 step 은 1이다)
        int min = dfs(maps, 1, 0, 0);
        return (min == Integer.MAX_VALUE) ? -1 : min;
    }

    private int dfs(int[][] maps, int steps, int positionY, int positionX) {
        int enemyY = maps.length - 1;
        int enemyX = maps[0].length - 1;
        if (visited[positionY][positionX] || maps[positionY][positionX] == 0) {
            return Integer.MAX_VALUE;
        }
        if (positionY == enemyY && positionX == enemyX) {
            return steps;
        }

        visited[positionY][positionX] = true;
        int min = Integer.MAX_VALUE;

        if (positionY < enemyY) {
            min = Math.min(min, dfs(maps, steps + 1, positionY + 1, positionX));
        }
        if (positionX < enemyX) {
            min = Math.min(min, dfs(maps, steps + 1, positionY, positionX + 1));
        }
        if (positionY > 0) {
            min = Math.min(min, dfs(maps, steps + 1, positionY - 1, positionX));
        }
        if (positionX > 0) {
            min = Math.min(min, dfs(maps, steps + 1, positionY, positionX - 1));
        }
        visited[positionY][positionX] = false;
        return min;
    }
}
