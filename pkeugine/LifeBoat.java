import java.util.Arrays;

public class LifeBoat {
    public static void main(String[] args) {
        Solution solution = new Solution();

        // 3
        int[] firstPeople = {70, 50, 80, 50};
        int firstLimit = 100;
        System.out.println(solution.solution(firstPeople, firstLimit));

        // 3
        int[] secondPeople = {70, 80, 50};
        int secondLimit = 100;
        System.out.println(solution.solution(secondPeople, secondLimit));
    }
}

class Solution {

    public int solution(int[] people, int limit) {
        int answer = 0;
        int p = 0;
        int q = people.length - 1;

        Arrays.sort(people);

        while (p <= q) {
            if (people[p] + people[q] > limit) {
                q--;
                answer++;
                continue;
            }
            int weight = people[q];
            while (people[p] + weight <= limit && p != q) {
                weight += people[p];
                p++;
            }
            q--;
            answer++;
        }

        return answer;
    }
}
