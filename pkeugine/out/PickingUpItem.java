import java.util.Queue;
import java.util.LinkedList;

public class PickingUpItem {
    // 프로그래머
    // 아이템 줍기
    public static void main(String[] args) {
        Solution solution = new Solution();

        int[][] rectangle1 = {{1,1,7,4}, {3,2,5,5}, {4,3,6,9}, {2,6,8,8}};
        int characterX1 = 1;
        int characterY1 = 3;
        int itemX1 = 7;
        int itemY1 = 8;
        // 17
        System.out.println(solution.solution(rectangle1, characterX1, characterY1, itemX1, itemY1));

        int[][] rectangle2 = {{1,1,8,4}, {2,2,4,9}, {3,6,9,8}, {6,3,7,7}};
        int characterX2 = 9;
        int characterY2 = 7;
        int itemX2 = 6;
        int itemY2 = 1;
        // 11
        System.out.println(solution.solution(rectangle2, characterX2, characterY2, itemX2, itemY2));

        int[][] rectangle3 = {{1,1,5,7}};
        int characterX3 = 1;
        int characterY3 = 1;
        int itemX3 = 4;
        int itemY3 = 7;
        // 9
        System.out.println(solution.solution(rectangle3, characterX3, characterY3, itemX3, itemY3));

        int[][] rectangle4 = {{2,1,7,5}, {6,4,10,10}};
        int characterX4 = 3;
        int characterY4 = 1;
        int itemX4 = 7;
        int itemY4 = 10;
        // 15
        System.out.println(solution.solution(rectangle4, characterX4, characterY4, itemX4, itemY4));

        int[][] rectangle5 = {{2,2,5,5}, {1,3,6,4}, {3,1,4,6}};
        int characterX5 = 1;
        int characterY5 = 4;
        int itemX5 = 6;
        int itemY5 = 3;
        // 10
        System.out.println(solution.solution(rectangle5, characterX5, characterY5, itemX5, itemY5));
    }
}

class Solution {

    private int answer;
    private int[][] map;

    private int[] dx = {1, 0, 0, -1};
    private int[] dy = {0, 1, -1, 0};

    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        answer = 0;
        map = new int[101][101];
        for (int i = 0; i < rectangle.length; i++) {
            fill(rectangle[i][0] * 2, rectangle[i][1] * 2, rectangle[i][2] * 2, rectangle[i][3] * 2);
        }
        bfs(characterX * 2, characterY * 2, itemX * 2, itemY * 2);
        answer /= 2;
        return answer;
    }

    private void fill(int x1, int y1, int x2, int y2) {
        for (int i = x1; i <= x2; i++) {
            for (int j = y1; j <= y2; j++) {
                if (map[i][j] == 2) {
                    continue;
                }
                map[i][j] = 2;
                if (i == x1 || i == x2 || j == y1 || j == y2) {
                    map[i][j] = 1;
                }
            }
        }
    }

    private void bfs(int startX, int startY, int itemX, int itemY) {
        boolean[][] visited = new boolean[101][101];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(startX);
        queue.add(startY);

        while (!queue.isEmpty()) {
            int x = queue.poll();
            int y = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (outOfBoundary(nx, ny)) {
                    continue;
                }
                if (map[nx][ny] != 1) {
                    continue;
                }
                if (visited[nx][ny]) {
                    continue;
                }

                map[nx][ny] = map[x][y] + 1;
                if (nx == itemX && ny == itemY) {
                    if (answer == 0) {
                        answer = map[nx][ny];
                    } else {
                        answer = Math.min(answer, map[nx][ny]);
                    }
                    continue;
                }
                visited[nx][ny] = true;
                queue.add(nx);
                queue.add(ny);
            }
        }
    }

    private boolean outOfBoundary(int x, int y) {
        return x < 0 || y < 0 || x > 100 || y > 100;
    }
}
