import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class TripPath {

    // 프로그래머스
    // 여행경로
    public static void main(String[] args) {
        Solution solution = new Solution();

        // ["ICN", "JFK", "HND", "IAD"]
        String[][] tickets1 = {{"ICN", "JFK"}, {"HND", "IAD"}, {"JFK", "HND"}};
        String[] results = solution.solution(tickets1);
        for (String ticket : results) {
            System.out.println(ticket);
        }
        System.out.println();

        // ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
        String[][] tickets2 = {{"ICN", "SFO"}, {"ICN", "ATL"}, {"SFO", "ATL"}, {"ATL", "ICN"}, {"ATL","SFO"}};
        String[] results2 = solution.solution(tickets2);
        for (String ticket : results2) {
            System.out.println(ticket);
        }
    }
}

class Solution {

    private List<String> answers;
    private boolean[] used;

    public String[] solution(String[][] tickets) {
        answers = new ArrayList<>();
        used = new boolean[tickets.length];

        dfs(0, "ICN", "ICN", tickets);

        Collections.sort(answers);
        return answers.get(0).split(" ");
    }

    private void dfs(int count, String currentAirport, String currentPath, String[][] tickets) {
        if (count == tickets.length) {
            answers.add(currentPath);
            return;
        }
        for (int i = 0; i < tickets.length; i++) {
            if (!used[i] && tickets[i][0].equals(currentAirport)) {
                used[i] = true;
                dfs(count + 1, tickets[i][1], String.format("%s %s", currentPath, tickets[i][1]), tickets);
                used[i] = false;
            }
        }
    }
}
