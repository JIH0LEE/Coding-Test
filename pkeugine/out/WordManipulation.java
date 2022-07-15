public class Main {

    // 프로그래머스
    // 단어 변환
    public static void main(String[] args) {
        Solution solution = new Solution();

        //4
        String firstBegin = "hit";
        String firstTarget = "cog";
        String[] firstWords = {"hot", "dot", "dog", "lot", "log", "cog"};
        System.out.println(solution.solution(firstBegin, firstTarget, firstWords));

        //0
        String secondBegin = "hit";
        String secondTarget = "cog";
        String[] secondWords = {"hot", "dot", "dog", "lot", "log"};
        System.out.println(solution.solution(secondBegin, secondTarget, secondWords));
    }
}

class Solution {

    private boolean[] visited;
    private int answer;

    public int solution(String begin, String target, String[] words) {
        visited = new boolean[words.length];
        answer = 0;
        dfs(begin, target, words, 0);
        return answer;
    }

    public void dfs(String begin, String target, String[] words, int count) {
        if (begin.equals(target)) {
            answer = count;
            return;
        }
        for (int i = 0; i < words.length; i++) {
            if (visited[i]) {
                continue;
            }
            int same = 0;
            for (int j = 0; j < begin.length(); j++) {
                if (begin.charAt(j) == words[i].charAt(j)) {
                    same++;
                }
            }
            if (same == begin.length() - 1) {
                visited[i] = true;
                dfs(words[i], target, words, count + 1);
                visited[i] = false;
            }
        }
    }
}
