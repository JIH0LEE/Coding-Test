import java.util.Arrays;

// 프로그래머스
// 완주하지 못한 선수
public class NotFinishedAthlete {

    public static void main(String[] args) {
        Solution solution = new Solution();

        // "leo"
        String[] firstParticipant = {"leo", "kiki", "eden"};
        String[] firstCompletion = {"eden", "kiki"};
        System.out.println(solution.solution(firstParticipant, firstCompletion));
        // "vinko"
        String[] secondParticipant = {"marina", "josipa", "nikola", "vinko", "filipa"};
        String[] secondCompletion = {"josipa", "filipa", "marina", "nikola"};
        System.out.println(solution.solution(secondParticipant, secondCompletion));
        // "mislav"
        String[] thirdParticipant = {"mislav", "stanko", "mislav", "ana"};
        String[] thirdCompletion = {"stanko", "ana", "mislav"};
        System.out.println(solution.solution(thirdParticipant, thirdCompletion));
    }
}

class Solution {

    public String solution(String[] participant, String[] completion) {
        Arrays.sort(participant);
        Arrays.sort(completion);

        int completionLength = completion.length;
        for (int i = 0; i < completionLength; i++) {
            if (!participant[i].equals(completion[i])) {
                return participant[i];
            }
        }

        return participant[participant.length - 1];
    }
}

