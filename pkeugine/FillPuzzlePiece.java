import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;

public class FillPuzzlePiece {

    // 프로그래머스
    // 퍼즐 조각 채우기
    public static void main(String[] args) {
        Solution solution = new Solution();

        //14
        int[][] game_board1 = {{1,1,0,0,1,0},{0,0,1,0,1,0},{0,1,1,0,0,1},{1,1,0,1,1,1},{1,0,0,0,1,0},{0,1,1,1,0,0}};
        int[][] table1 = {{1,0,0,1,1,0},{1,0,1,0,1,0},{0,1,1,0,1,1},{0,0,1,0,0,0},{1,1,0,1,1,0},{0,1,0,0,0,0}};
        System.out.println(solution.solution(game_board1, table1));

        // 0
        int[][] game_board2 = {{0,0,0},{1,1,0},{1,1,1}};
        int[][] table2 = {{1,1,1},{1,0,0},{0,0,0}};
        System.out.println(solution.solution(game_board2, table2));
    }
}

class Solution {

    private List<List<Point>> emptys;
    private List<List<Point>> blocks;

    private boolean[][] visited;
    private int boardSize;

    private int[] dx = {1, 0, 0, -1};
    private int[] dy = {0, -1, 1, 0};

    public int solution(int[][] game_board, int[][] table) {
        int answer = 0;
        boardSize = game_board.length;
        visited = new boolean[boardSize][boardSize];

        emptys = new ArrayList<>();
        blocks = new ArrayList<>();

        for (int i = 0; i < boardSize; i++) {
            for (int j = 0; j < boardSize; j++) {
                if (game_board[i][j] == 0 && !visited[i][j]) {
                    emptys.add(bfs(game_board, i, j, 0));
                }
            }
        }

        for (int i = 0; i < boardSize; i++) {
            Arrays.fill(visited[i], false);
        }

        for (int i = 0; i < boardSize; i++) {
            for (int j = 0; j < boardSize; j++) {
                if (table[i][j] == 1 && !visited[i][j]) {
                    blocks.add(bfs(table, i, j, 1));
                }
            }
        }

        boolean[] filledBoard = new boolean[emptys.size()];
        for (int i = 0; i < blocks.size(); i++) {
            List<Point> block = blocks.get(i);
            for (int j = 0; j < emptys.size(); j++) {
                List<Point> empty = emptys.get(j);

                if (block.size() == empty.size() && !filledBoard[j]) {
                    if (rotatable(block, empty)) {
                        answer += block.size();
                        filledBoard[j] = true;
                        break;
                    }
                }
            }
        }
        return answer;
    }

    private List<Point> bfs(int[][] map, int x, int y, int filled) {
        Queue<Point> queue = new LinkedList<>();
        List<Point> result = new ArrayList<>();

        queue.add(new Point(x, y));
        visited[x][y] = true;

        result.add(new Point(0, 0));

        while (!queue.isEmpty()) {
            Point current = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nx = current.x + dx[i];
                int ny = current.y + dy[i];

                if (nx >= 0 && nx < boardSize && ny >= 0 && ny < boardSize) {
                    if (!visited[nx][ny] && map[nx][ny] == filled) {
                        visited[nx][ny] = true;
                        queue.add(new Point(nx, ny));

                        result.add(new Point(nx - x, ny - y));
                    }
                }
            }
        }

        Collections.sort(result);
        return result;
    }

    private boolean rotatable(List<Point> block, List<Point> empty) {
        for (int i = 0; i < 4; i++) {
            int zeroX = block.get(0).x;
            int zeroY = block.get(0).y;

            for (int j = 0; j < block.size(); j++) {
                block.get(j).x -= zeroX;
                block.get(j).y -= zeroY;
            }

            boolean fit = true;

            for (int j = 0; j < empty.size(); j++) {
                Point emptyPoint = empty.get(j);
                Point blockPoint = block.get(j);

                if (emptyPoint.x != blockPoint.x || emptyPoint.y != blockPoint.y) {
                    fit = false;
                    break;
                }
            }

            if (fit) {
                return true;
            } else {
                for (int j = 0; j < block.size(); j++) {
                    int temp = block.get(j).x;

                    block.get(j).x = block.get(j).y;
                    block.get(j).y = -temp;
                }

                Collections.sort(block);
            }
        }
        return false;
    }
}

class Point implements Comparable<Point> {

    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Point o) {
        if (this.x == o.x) {
            return this.y - o.y;
        }
        return this.x - o.x;
    }
}
