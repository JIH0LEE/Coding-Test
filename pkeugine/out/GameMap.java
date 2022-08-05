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

    public int solution(int[][] maps) {
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
