import java.util.Queue;
import java.util.LinkedList;

public class Main {

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

    // 상대팀 진영은 항상 배열의 가장 마지막 부분인가...?
    public int solution(int[][] maps) {
        int Y = maps.length;
        int X = maps[0].length;
        boolean[][] visited = new boolean[Y][X];
        Queue<Point> q = new LinkedList<>();

        int y = 0;
        int x = 0;
        int size = 0;
        int count = 0;

        Point point = new Point();
        q.add(new Point(X-1, Y-1));

        while(!q.isEmpty()) {
            size = q.size();
            count++;
            for (int i = 0; i < size; i++) {
                point = q.peek();
                x = point.getX();
                y = point.getY();
                q.remove();

                if(visited[y][x]) {
                    continue;
                }
                maps[y][x] = 0;
                visited[y][x] = true;
                if (x == 0 && y == 0) {
                    return count;
                }
                if (x > 0 && maps[y][x-1] == 1) {
                    q.add(new Point(x-1, y));
                }
                if (y > 0 && maps[y-1][x] == 1) {
                    q.add(new Point(x, y-1));
                }
                if (x < X - 1 && maps[y][x+1] == 1) {
                    q.add(new Point(x+1, y));
                }
                if (y < Y - 1 && maps[y+1][x] == 1) {
                    q.add(new Point(x, y+1));
                }
            }

        }
        return -1;
    }
}

class Point {

    private final int x;
    private final int y;

    public Point() {
        this.x = 0;
        this.y = 0;
    }

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return this.x;
    }

    public int getY() {
        return this.y;
    }
}
