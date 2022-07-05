// 프로그래머스
// 조이스틱
public class Joystick {

    public static void main(String[] args) {
        Solution solution = new Solution();

        // 56
        System.out.println(solution.solution("JEROEN"));

        // 23
        System.out.println(solution.solution("JAN"));
    }
}

class Solution {

    public int solution(String name) {
        int answer = 0;
        int length = name.length();
        int move = length - 1;
        int index = 0;

        for (int i = 0; i < length; i++) {
            char target = name.charAt(i);
            answer += Math.min(target - 'A', 'Z' - target + 1);

            index = i + 1;
            while(index < length && name.charAt(index) == 'A') {
                index++;
            }

            move = Math.min(move, i * 2 + length - index);
            // check opposite direction
            move = Math.min(move, (length - index) * 2 + i);
        }
        answer += move;

        return answer;
    }
}
